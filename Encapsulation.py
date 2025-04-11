#Encapsulation -Implement Secure Bank Account
#class -secure
#methods -getbalance,deposit,withdraw,changepin

class secure:
    def __init__(self,name,pin,balance=0):
        self.name=name
        self.__pin=pin
        self.__balance=balance
    def getbalance(self,pin):
        if pin==self.__pin:
            return self.__balance
        else:
            return "Access Denied : Invalid Pin"
    def deposit(self,amount):
        self.amount=amount
        if amount>0:
            self.__balance+=amount
            print(f"Deposited {amount}")
        else:
            print("Insufficient deposited amount")
    def withdraw(self,amount):
        if amount<=0:
            print("Can't withdraw amount")
        elif amount>self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance-=amount
            print(f"Withdrawal {amount}")
    def changepin(self,oldpin,newpin):
        if oldpin==self.__pin:
            self.__pin=newpin
            print("Pin Updated Successfully")
        else:
            print("Pin Invalid Can't Update please enter correct pin")
acc = secure("Ravi", 4321, 1000)
print(acc.getbalance(1111))     
print(acc.getbalance(4321))     
acc.deposit(500)
acc.withdraw(2000)              
acc.withdraw(-100)               
acc.changepin(1234, 9999)
acc.changepin(4321, 9999)
        
        
            
