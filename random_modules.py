import random

'''
methods available in random
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence',
'__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
'_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index', '_inst', '_isfinite', 
'_lgamma', '_log', '_log2', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', 
'_urandom', '_warn', 'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss',
'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 
'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
'''
# to create an random integer with in a range
int_number = random.randint(1,6)
print(F"{int_number}")

int_low = 1
int_high = 100
int_number = random.randint(int_low,int_high)
print(F"{int_number}")

# to create an random floating point number b/w 0 and 1
print(random.random())
# choices
tuple_options = ("Rock","Paper","Scissors")

str_option = random.choice(tuple_options)
print(str_option)

# shuffle method
list_card = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
random.shuffle(list_card)
print(list_card)

'''
Python number guessing game
'''

int_low = 0
int_high = 100
int_answer = random.randint(int_low,int_high)
int_no_of_guesses = 0

bln_running = True

print("Welcome to number guessing game ..!")
print(f"Enter a number between {int_low} and {int_high}")

while bln_running:
    str_guess = input("Enter a number : ")
    
    if str_guess.isdigit():
        int_guess = int(str_guess)
        int_no_of_guesses += 1
        
        if int_guess < int_low or int_guess > int_high:
            print("The number is out of range")
        elif int_guess < int_answer:
            print("Entered value is too Low ! Try again ")
        elif int_guess > int_answer:
            print("Entered value is too High ! Try again ")
        else:
            print(f"Hurray..... ! The answer is {int_answer} ")
            print(F"Took {int_no_of_guesses} to correct.....")


    else:
        print("Entered Value is not valid")
        
'''
Rock Paper Scissors Game
'''

tuple_options = ("Rock","Paper","Scissors")
bln_continue = True
while bln_continue:
    str_player_option = None
    str_computer_option = random.choice(tuple_options)

    while str_player_option not in tuple_options:
        str_player_option = input("Enter a Choice ('Rock','Paper','Scissors') : ")
        
    if str_player_option == str_computer_option:
        print("It's a tie")
    elif str_player_option == "Paper" and str_computer_option == "Rock":
        print("You win..!")
    elif str_player_option == "Rock" and str_computer_option =="Scissors":
        print("You win..!")
    elif str_player_option == "Scissors" and str_computer_option == "Paper":
        print("You win..!")
    else:
        print("You loose..!")
    
    print(f"player: {str_player_option}")
    print(f"computer: {str_computer_option}")
    
    if input("Play again (y/n) ?: ").lower() != "y":
        bln_continue = False