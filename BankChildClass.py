from UserMainClass import ValueTypeError
from UserMainClass import User
class Bank(User):
    '''Balnk Class inheret user class'''
    def __init__(self,name,age,gender,user_id,password,amount):
        '''object Initalization:
        Args: 
            name 'string': user name
            age 'number': user age 
            gender 'string': gender
            user_id 'string or number': user id
            password 'string or number': user password 
            amount 'number': amount 
        '''
        super().__init__(name,age,gender,user_id,password)
        self.balance = amount 
        if isinstance(self.balance, str):
            raise ValueTypeError
            
    def deposit(self,amount):
        '''add amount
        Args:
            amount'number': number
        Return object balance
        '''
        if (type(amount) ==str):
            raise TypeError
        else: 
            self.balance +=amount
            return self.balance
        
    def withdraw(self,amount):
        '''withdraw amount
        Args:
            amount'number': number
        Return object balance
        '''
        if (type(amount) ==str):
            raise TypeError
        elif amount > self.balance:
            raise ValueError
        else: 
            self.balance -=amount
            return self.balance
        
    def get_user_info(self):
        '''print object information'''
        super().get_user_info()
        print(f'Account Balance: {self.balance}')
        
    def get_Balance(self):
        '''print object account balance'''
        print(f'Account Balance: {self.balance}')