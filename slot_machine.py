# python slot machine 
import random
# 
def spin_row():
    list_symbols = ["A","B","C","D","E"]
    list_result = [random.choice(list_symbols) for symbol in range(3)]
    return list_result

# 
def print_row(list_symbols:list):
    print("***********************")
    print(" | ".join(list_symbols))
    print("***********************")
    
# 
def get_payout(list_symbols:list,int_bet_amount:int):
    if list_symbols[0] == list_symbols[1] == list_symbols[2]:
        if list_symbols[0] == "A":
            return int_bet_amount * 2
        if list_symbols[0] == "B":
            return int_bet_amount * 3
        if list_symbols[0] == "c":
            return int_bet_amount * 4
        if list_symbols[0] == "D":
            return int_bet_amount * 5
        if list_symbols[0] == "E":
            return int_bet_amount * 6
    else:
        return 0


# 
def main():
    dbl_balance = 100000000
    print("***********************")
    print("Welcome to Python slot ")
    print("Symbols: A,B,C,D,E")
    print("***********************")
    
    while dbl_balance > 0:
        print(f" Your current balance is {dbl_balance}")
        
        str_bet = input("Please enter your bet amount : ")
        
        if not str_bet.isdigit():
            print("Please enter a valid number")
            continue
        int_bet_amount = int(str_bet)
        
        if int_bet_amount > dbl_balance:
            print(f"Insufficeint Balance {dbl_balance}")
            continue
        if int_bet_amount <= 0 :
            print(f"Amount should be greater than zero. {int_bet_amount}")
            continue
        
        dbl_balance -= int_bet_amount
        list_result = spin_row()
        print_row(list_result)
        int_payout_amount = get_payout(list_result,int_bet_amount) 
        
        if int_payout_amount > 0 :
            print("You Won ")
            dbl_balance += int_payout_amount
        else :
            print("Bad luck ..! try again")
            
        if input("Play agan . . . ! (Y/N) ?: ").upper() != "Y":
            break
    
    print(F"Game over you balance is {dbl_balance}")   

if __name__ == "__main__":
    main()
