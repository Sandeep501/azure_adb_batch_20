# encapsulation

class BankAccount:
    __new_balance = 2000
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # -- private variable
    
    def deposit(self, amount):
        self.__balance += amount
        # self.__balance = self.__balance + amount
        return f"Deposited {amount}. New Balance: {self.__balance}"
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient Balance"
        
        self.__balance -= amount
        return f"withdraw of {amount} is successful. New Balance: {self.__balance}"
    
    def __get_balance(self):
        return f"balance is: {self.__balance}"
    
    def display__balance(self):
        return self.__get_balance()
    

account = BankAccount("Sandeep", 1000)

print(account.deposit(500))
print(account.withdraw(200))
print(account.display__balance())