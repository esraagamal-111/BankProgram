from UserMainClass import ValueTypeError
from UserMainClass import User
from BankChildClass import Bank

def create_user(name,age,gender,user_id,password,amount):
    '''create new user/object:
        Args: 
            name 'string': user name
            age 'number': user age 
            gender 'string': gender
            user_id 'string or number': user id
            password 'string or number': user password 
            amount 'number': amount 
        '''
    try:
        new_user = Bank(name,age,gender,user_id,password,amount)
    except ValueTypeError:
        print ('User Not created, Age and Amount should be a number')
    else:
        print("User Created Successfuly")
        return new_user

def user_info(user):
    '''print user information with handling error'''
    try:
        user.get_user_info()
    except AttributeError:
        print ('User Not Difined')


def user_Balance(user):
    '''print user account balance with handling error'''
    try:
        user.get_Balance()
    except AttributeError:
        print ('User Not Difined')


def deposit(user,amount):
    '''add amount
        Args:
            amount'number': number
        Return object balance
        '''
    try:
        user.deposit(amount)
    except TypeError:
        print ('Amount should be a number')
    finally:
        print(f'Balance: {user.balance}')


def withdraw(user,amount):
    '''withdraw amount
        Args:
            amount'number': number
        Return object balance
        '''
    try:
        user.withdraw(amount)
    except TypeError:
        print ('Amount should be a number')
    except ValueError :
        print ('Amount should equal than or less to your balance')
        
    finally:
        print(f'Balance: {user.balance}')



def main():
    '''running Bank program'''
    try:
        name = input("please Enter your name: ")
        age = float(input('please Enter Your Age: '))
        gender = input("please Enter Your gender: ")
        amount = float(input("please Enter deposit Amount: "))
        user_id = input("please Enter Your ID: ")
        password = input("please Enter password: ")
        
    except ValueError: 
        print("Invalid Data , Age or Amount Type Should be a Number.")
        try_again = input("Do you want to try again, Enter Y or N: ").upper()
        if try_again == "Y":
            main()
        else:
            print("Program Exit , See you next time")
        
    else:
        new_user = create_user(name,age,gender,user_id,password,amount)
        done=False
        while done==False:
            print(""" ======LIBRARY MENU=======

                      1. Check Account Information
                      2. Check Account Balance
                      3. Deposite
                      4. Withraw
                      5. Signout
                      0.Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice == 1:
                if new_user.check_password():
                    user_info(new_user)
                else:
                    try_again = input("Password Error, Do you want to try again ?!, Enter 'Y' or 'N': ").upper()
                    if try_again == "Y":
                        continue
                    else:
                        print("Program Exit , See you next time")
                        break
                        
            elif choice == 2:
                if new_user.check_password():
                    user_Balance(new_user)
                else:
                    try_again = input("Password Error, Do you want to try again ?!, Enter 'Y' or 'N': ").upper()
                    if try_again == "Y":
                        continue
                    else:
                        print("Program Exit , See you next time")
                        break
            elif choice == 3:
                if new_user.check_password():
                    amount = float(input("please Enter Amount: "))
                    deposit(new_user,amount)
                else:
                    try_again = input("Password Error, Do you want to try again ?!, Enter 'Y' or 'N': ").upper()
                    if try_again == "Y":
                        continue
                    else:
                        print("Program Exit , See you next time")
                        break
            elif choice == 4:
                if new_user.check_password():
                    amount = float(input("please Enter Amount: "))
                    withdraw(new_user,amount)
                else:
                    try_again = input("Password Error, Do you want to try again ?!, Enter 'Y' or 'N': ").upper()
                    if try_again == "Y":
                        continue
                    else:
                        print("Program Exit , See you next time")
                        break
                
            elif choice == 5:
                print(f'Sigining Out, see u next time {name}')
                main()
            elif choice == 0:
                print('program exit, see u next time')
                break
            else:
                try_again = input("Invalid Choice, Do you want to try again ?!, Enter 'Y' or 'N': ").upper()
                if try_again == "Y":
                    continue
                else:
                    print("Program Exit , See you next time")
                    break