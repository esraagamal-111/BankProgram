class ValueTypeError(Exception): 
    '''class to handle exception'''
    pass

class User():
    '''User Class'''
    def __init__(self,name,age,gender,user_id,password):
        '''object Initalization:
        Args: 
            name 'string': user name
            age 'number': user age 
            gender 'string': gender
            user_id 'string or number': user id
            password 'string or number': user password 
        '''
        print (f'trying to create new user name: {name}, age: {age}, gender: {gender}')
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.user_id = user_id
        self.password = password
        if isinstance(self.age, str):
            raise ValueTypeError
            
#     def __del__(self):
#         print(f'__del__ {self.name}')

    def delete(self):
        ''' delete object'''
        print(f'__del__ {self.name}')
             
    def get_user_info(self):
        '''print object information'''
        print(f'User name: {self.name}\nAge:{self.age}\nGender:{self.gender}')
    
    def check_password(self):
        ''' check object password
        Args:
            password 'string or number': password
        Return boolean 
        '''
        confirm_password = input("please Enter Your password: ")
        return self.password == confirm_password