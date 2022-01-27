class Bank:

    def __init__(self, balance: List[int]):
        self.balance = [0] + balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.n or account2 > self.n:
            return False
        if self.balance[account1] >= money:
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account > self.n:
            return False
        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.n:
            return False
        if self.balance[account] < money:
            return False
        self.balance[account] -= money
        return True
