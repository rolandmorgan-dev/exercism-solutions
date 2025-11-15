import json
from collections import defaultdict


class RestAPI:
    def __init__(self, database: dict[str, list[dict[str, object]]] | None = None):
        self.database = database or {"users": []}

    def _add_user(self, user) -> dict[str, object]:
        """Add a new user to the database with default balances."""
        user = {"name": user, "owes": {}, "owed_by": {}, "balance": 0.0}
        self.database["users"].append(user)
        return user

    def _process_iou(self, lender, borrower, amount) -> list[dict[str, object]]:
        """
        Process an IOU transaction between a lender and a borrower.

        Adjusts balances and debt relationships accordingly.
        Returns a sorted list of the two affected users, each as a dictionary.
        """
        changed_data = []
        for user in self.database["users"]:
            if user["name"] not in (lender, borrower):
                continue

            user["owes"] = defaultdict(float, user["owes"])
            user["owed_by"] = defaultdict(float, user["owed_by"])

            if user["name"] == lender:
                user["balance"] += amount
                user["owes"][borrower] -= amount
                if user["owes"][borrower] <= 0:
                    user["owed_by"][borrower] += abs(user["owes"][borrower])  
            else:
                user["balance"] -= amount
                user["owed_by"][lender] -= amount
                if user["owed_by"][lender] <= 0:
                    user["owes"][lender] += abs(user["owed_by"][lender])

            # Remove zero or negative debt persons from owes and owed_by
            for key in ["owes", "owed_by"]:
                user[key] = {name: val for name, val in user[key].items() if val > 0}

            changed_data.append(user)

        return sorted(changed_data, key=lambda user: user["name"])

    def get(self, url, payload=None):
        """Handle GET requests: return only the users specified in the payload."""
        if payload:
            names = json.loads(payload).get("users", [])
            users = [user for user in self.database["users"] if user["name"] in names]

        return json.dumps({"users": users if payload else []})

    def post(self, url, payload=None):
        """Handle POST requests: return updated data for the affected users."""
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
