# Python banking program

# 
def show_balance(dbl_balance,str_process:str=""):
    print(f"Your Current Balance is {dbl_balance} {f"after {str_process}" if str_process else ""}")

# add amount to current balance
def deposit(dbl_amount:float):
    if dbl_amount <= 0: 
        print("Amount must be greater than 0")
        return 0
    else: 
        return dbl_amount
# deduct amount from balance
def withdraw(dbl_amount:float,dbl_balance):
    if dbl_amount > dbl_balance:
        print("Insuffiecent Balance")
        return 0
    elif dbl_amount <= 0: 
        print("Amount must be greater than 0")
        return 0
    else: 
        return dbl_amount

# 
def main():
    dbl_balance = 0
    bln_running = True

    while bln_running:
        print("Banking Program")
        print("1. Show Balance ")
        print("2. Deposit ")
        print("3. Withdraw ")
        print("4. Exit ")
        
        str_choice = input("Enter Your Choice (1-4): ")
        if str_choice == '1':
            show_balance(dbl_balance)
        elif str_choice == '2':
            dbl_balance += deposit(float(input("Enter an amount to deposit : ")))
            show_balance(dbl_balance,"depost.")

        elif str_choice == '3':
            dbl_balance -= withdraw(float(input("Enter an amount to withdraw: ")),dbl_balance)
            show_balance(dbl_balance,"withdraw.")

        elif str_choice == '4':
            bln_running = False
            print("Exited")
        else:
            print("Invalid choice Try againg")

if __name__ == "__main__":
    main()