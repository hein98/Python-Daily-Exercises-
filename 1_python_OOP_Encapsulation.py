class Bank:
    def __init__(self,original_balance):
        self.__original_balance=original_balance
      
        
    def deposit(self,new_balance):
        self.__original_balance=new_balance+self.__original_balance
        print(f'Now your balance is {self.__original_balance}')
        
    def withdraw(self,withdraw_amount):
        
        if withdraw_amount>self.__original_balance:
            print('Invalid Withdrawal')
        if withdraw_amount < self.__original_balance:  
            print(f'You withdrawed {self.__original_balance - withdraw_amount}')
        else:
            print('Pls make a proper withdrawal')
            
    def get_my_balance(self):
        return self.__original_balance
    
new_account=Bank(300)
print(new_account.get_my_balance())
print(new_account.__original_balance())#Error,private attribute with '__' double underscre
new_account.deposit(50)  
new_account.withdraw(50)
