# program to create a class
class BankAccount:
    def __init__(self, bank_name, account_number, bvn, initial_amount):
        self.bank_name = bank_name
        self.acc_number = account_number
        self.bvn = bvn
        self.balance = initial_amount
        
# defining a deposit methods of the class
    def deposit(self, amount):
        self.balance += amount
        
# defining a withdrawal method of the class
    def withdraw(self, amount):
        self.balance -= amount
        
# to get the balance method
def get_balance(self):
        return self._balance
        
# using the dump()method to store objects in a file
def dump(self):
    s = '%s, %s, balance: %s' % \
        (self.bank_name, self.acc_name, self.bvn, self.balance)
    print(s)
    
# creating an object of the class
acc_holder1 = BankAccount('GTB', '0218492542', '29458902', 200000)
acc_holder2 = BankAccount('UBA', '3028495034', '34582984', 4000000)

acc_holder1.deposit(50000)
acc_holder1.withdraw(20000)

acc_holder2.deposit(34500)
acc_holder2.withdraw(23000)

print ('The account owner balance:', acc_holder1.balance)
