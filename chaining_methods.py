class User:

    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def display_user_balance(self):
        print(f"{self.name} has a balance of {self.balance}")
        return self

    def make_transfer(self, amount, friend):
        self.balance -= amount
        friend.balance += amount
        print(f"{self.name} has {self.balance} remaining. {friend.name} has {friend.balance} remaining.")
        return self

ernesto = User("Ernesto") 
michael = User("Michael")
henry = User("Henry")
ernesto.make_deposit(300).make_deposit(200).make_deposit(100).display_user_balance()
michael.make_deposit (200).make_deposit (200).make_withdrawal (100).make_withdrawal (200).display_user_balance()
henry.make_deposit (500).make_withdrawal (100).make_withdrawal (200).make_withdrawal (200).display_user_balance()
ernesto.make_transfer(200, michael)