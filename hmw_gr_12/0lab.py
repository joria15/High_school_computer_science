from datetime import datetime

def menu():
        print("Bank Account Menu: \n"
        "1. Deposit Money \n"
        "2. Withdraw Money (Overdraft Allowed) \n"
        "3. Check Balance \n"
        "4. Exit \n" 
        "5. History\n")
        opt = int(input("Enter a choice from 1-5: "))
        print("")
        return opt

def deposit_money(current):
    deposit = float(input("enter deposit amount: "))
    print("")
    if deposit > 100 or deposit < 0:
        print("Invalid input, between $0-100 only")
        return current
    else:
        new = deposit + current
        time = datetime.now()
        timestamp = time.strftime("%H:%M:%S")
        res_1 = f"Deposited: {deposit} Time: {timestamp}"
        return new, res_1

def withdraw_money(current):
    withdraw = float(input("enter withdrawal amount: "))
    print("")
    new = current - withdraw
    time = datetime.now()
    timestamp = time.strftime("%H:%M:%S")
    res_2 = f"Withdrew: {withdraw} Time: {timestamp}"
    return new, res_2

def balance_amount(current):
    print("")
    return print(f"Your current amount: {round(current, 2)} ")

def main():
    """
    Main loop of the program.

    Show menu options and prompt user for input.

    Repeat until user chooses to exit.
    """

    print("Welcome to my bank!")

    balance = 0.0
    history = []

    while True:
        
        opt = menu()

        if opt == 1:
            balance, res_1 = deposit_money(balance)
            history.append(res_1)

        elif opt == 2:
            balance, res_2 = withdraw_money(balance)
            history.append(res_2)

        elif opt == 3:
            balance_amount(balance)

        elif opt == 4:
            print("Thank you for banking with us!")
            break
        
        elif opt == 5:
            print(f"{history} \n")
        else:
            print("Invalid input \n")




if __name__ == '__main__':

    main()