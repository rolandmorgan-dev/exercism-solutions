from threading import Lock


class BankAccount:
    def __init__(self):
        self._active = False
        self._balance = 0
        self._lock = Lock()

    def open(self):
        self.validate("open")
        self._active = True

    def close(self):
        self.validate("close")
        self._active = False
        self._balance = 0

    def get_balance(self):
        self.validate("get_balance")
        return self._balance

    def deposit(self, amount):
        self.validate("deposit", amount)
        with self._lock:
            self._balance += amount

    def withdraw(self, amount):
        self.validate("withdraw", amount)
        with self._lock:
            self._balance -= amount

    def validate(self, command, amount=None):
        """
        Validates account state and operation-specific rules.
        Raises ValueError for invalid operations.
        """
        if command == "open" and self._active:
            raise ValueError("account already open")

        if command != "open" and not self._active:
            raise ValueError("account not open")

        if command == "withdraw" and self._balance < amount:
            raise ValueError("amount must be less than balance")

        if command in ("deposit", "withdraw") and amount <= 0:
            raise ValueError("amount must be greater than 0")
