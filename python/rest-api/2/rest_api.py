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
        with self.lock: # prevent race condition when multiple threads are adding users
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
            list[dict[str, object]]: Sorted list of updated user dictionaries.
            See class docstring for user dictionary format.
        """
        with self.lock: # coarse-grained locking method
            changed_data = []
            for user in self.database["users"]:
                if user["name"] not in (lender, borrower):
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

            return sorted(changed_data, key=lambda user: user["name"])

    def get(self, url, payload=None) -> str:
        """
        Handle GET request.

        Args:
            url (str): The requested URL (unused here, kept for interface).
            payload (str | None): JSON string containing query parameters of "users".

        Returns:
            str: JSON string with key "users" mapping to list of user dicts.
            See class docstring for user dict format.
        """
        if payload:
            names = json.loads(payload).get("users", [])
            users = [user for user in self.database["users"] if user["name"] in names]

        return json.dumps({"users": users if payload else []})

    def post(self, url, payload=None) -> str:
        """
        Handle POST request.

        Args:
            url (str): The endpoint URL ("/add" or "/iou").
            payload (str | None): JSON string containing request data.

        Returns:
            str: JSON string with key "users" mapping to updated or added user dicts.
            See class docstring for user dictionary format.
        """
        payload = json.loads(payload) if payload else {"users": []}
        data_added = None

        if url == "/add":
            if not any(u["name"] == payload["user"] for u in self.database["users"]):
                data_added = self._add_user(payload["user"])
        elif url == "/iou":
            lender = payload["lender"]
            borrower = payload["borrower"]
            amount = payload["amount"]
            data_added = {"users": self._process_iou(lender, borrower, amount)}

        return json.dumps(data_added or {"users": []})
