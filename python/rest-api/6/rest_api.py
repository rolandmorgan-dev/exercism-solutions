import json
from collections import defaultdict
import threading


class RestAPI:
    """
    A simple thread-safe REST API for managing users and IOUs.

    User dictionary format:
        {
            "name": str,
            "owes": dict[str, float],
            "owed_by": dict[str, float],
            "balance": float,
        }
    """
    def __init__(self, database: dict[str, list[dict[str, object]]] | None = None):
        self.database = database or {"users": []}
        self.lock = threading.Lock() # Ensures thread-safe access to shared data

    def _add_user(self, username) -> dict[str, object]:
        """
        Add a new user with default values to the database.

        Args:
            username (str): The name of the user to add.

        Returns:
            dict[str, object]: Newly created user dict. See class docstring for format.
        """
        user = {"name": username, "owes": {}, "owed_by": {}, "balance": 0.0}
        self.database["users"].append(user)
        return user

    def _process_iou(self, lender, borrower, amount) -> list[dict[str, object]]:
        """
        Process an IOU transaction between a lender and a borrower.

        Adjusts balances and debt relationships accordingly.
        Returns a sorted list of the two affected users, each as a dictionary.

        Args:
            lender (str): The name of the lender.
            borrower (str): The name of the borrower.
            amount (float): The amount of the IOU.

        Returns:
            list[dict[str, object]]: Sorted list of updated user dicts.
            See class docstring for user dictionary format.
        """
        with self.lock: # Coarse-grained locking method
            changed_data = []
            updated_users = 0
            names = {lender, borrower} # Set of user names in the current IOU process
            for user in self.database["users"]:
                if user["name"] not in names:
                    continue

                user["owes"] = defaultdict(float, user["owes"])
                user["owed_by"] = defaultdict(float, user["owed_by"])

                if user["name"] == lender:
                    user["balance"] += amount
                    user["owes"][borrower] -= amount
                    if user["owes"][borrower] < 0:
                        user["owed_by"][borrower] += abs(user["owes"][borrower])
                else:
                    user["balance"] -= amount
                    user["owed_by"][lender] -= amount
                    if user["owed_by"][lender] < 0:
                        user["owes"][lender] += abs(user["owed_by"][lender])

                # Remove zero or negative debt persons from owes and owed_by
                for key in ["owes", "owed_by"]:
                    user[key] = {name: v for name, v in user[key].items() if v > 0}

                changed_data.append(user)
                
                updated_users += 1
                if updated_users == 2: # Early exit from the loop
                    break

            return sorted(changed_data, key=lambda user: user["name"])

    def get(self, url, data=None) -> str:
        """
        Handle GET request.

        Args:
            url (str): The requested URL (unused here, kept for interface).
            data (str | None): JSON string containing query parameters of "users".

        Returns:
            str: JSON string with key "users" mapping to list of user dicts.
            See class docstring for user dictionary format.
        """
        if data:
            names = json.loads(data).get("users", [])
            users = [user for user in self.database["users"] if user["name"] in names]

        return json.dumps({"users": users if data else []})

    def post(self, url, data=None) -> str:
        """
        Handle POST request.

        Args:
            url (str): The endpoint URL ("/add" or "/iou").
            data (str | None): JSON string containing request data.

        Returns:
            str: JSON string with key "users" mapping to updated or added user dicts.
            See class docstring for user dictionary format.
        """
        data = json.loads(data) if data else {"users": []}
        data_added = None

        if url == "/add":
            # Prevent race condition when multiple threads try to add a user
            with self.lock:
                if not any(u["name"] == data["user"] for u in self.database["users"]):
                    data_added = self._add_user(data["user"])
        elif url == "/iou":
            lender = data["lender"]
            borrower = data["borrower"]
            amount = data["amount"]
            data_added = {"users": self._process_iou(lender, borrower, amount)}

        return json.dumps(data_added or {"users": []})
