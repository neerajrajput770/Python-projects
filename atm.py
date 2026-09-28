
class ATM:
    def __init__(self):
        self.__balance = 5000

    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount      
        else:
            print("Invalid Amount")
            
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

atm = ATM()
print(atm.get_balance())
depo = int(input("Enter Deposite Amount..."))
atm.deposit(depo)
print(atm.get_balance())
withd = int(input("Enter Withdraw Amount..."))
atm.withdraw(withd)
print(atm.get_balance())
print('Thank You!')