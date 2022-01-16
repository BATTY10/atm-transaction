
def show_balance(balance):
    print("Available Balance:",balance)
def deposit(balance):
    dep_amt= float(input("Enter amount to deposit:"))
    return balance + dep_amt
def withdraw(balance):
    with_amt= float(input("Enter amount to withdraw:"))
    if balance < float(with_amt):
        print("Insufficient Balance")
        return balance
    return balance - with_amt
def logout(name):
    print("Goodbye",name)


