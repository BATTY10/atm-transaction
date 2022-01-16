import sys
from banking_pkg import account
def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
print("          === Automated Teller Machine ===          ")
while True:
    name=str(input("Enter name to register: " ))
    if len(name)>10:
        print("The maximun character allowed is 10.")
    elif len(name)==0:
        print("Name column can not be blank")
    else:
        break
while True:
    pin=(input("Enter PIN:"))
    if len(pin)>4 or len(pin)<4:
        print("pin must be 4 numbers")
    else:
        break
balance= 0
print("Enter name to register:",name)
print("Enter PIN:",pin)
print(name ,"has been registered with a starting balance of $",balance)

transaction_on=True

while transaction_on==True:

    while True:
        print("LOGIN")
        name_to_validate=str(input("Enter name : " ))
        pin_to_validate=(input("Enter PIN:"))
        if name==name_to_validate and pin==pin_to_validate:
            print("Login successfully!")
            break        
        else:
            print("Invalid credentials!")

    while True:
        atm_menu(name)
        option = input("Choose an option:")
        if option=="1":
            account.show_balance(balance)
        if option=="2":
           balance= account.deposit(balance)
           account.show_balance(balance)
        if option=="3":
            balance=account.withdraw(balance)
            account.show_balance(balance)
        if option =="4":
            account.logout(name)
        break
    value=input("Do you wish to perform another transaction? Y/N:").lower() 
    while True:
        if value =="n":
            sys.exit()
        else:
            break
         
        
        
               
    





        



    


