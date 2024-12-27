import random
# to-do add more wors
tuple_words = ("apple","banana","orange","pineapple","grapes","cocunut")

# Dictionary with Key :int Value tuple
dict_hangman_art = {
                    0:("   ",
                       "   ",
                       "   "),
                    
                    1:(" O ",
                       "   ",
                       "   "),
                    
                    2:(" 0 ",
                       " | ",
                       "   "),
                    
                    3:(" O ",
                       "/| ",
                       "   "),
                    
                    4:(" O ",
                       "/|\\",
                       "   "),
                    
                    5:(" O ",
                       "/|\\",
                       "/  "),
                    
                    6:(" O ",
                       "/|\\",
                       "/ \\"),   
}

    
def display_man(int_wrong_guess:int):
    for line in dict_hangman_art[int_wrong_guess]:
        print(line)
        
def display_hint(str_hint:str):
    print(" ".join(str_hint))
    
def display_answer(str_answer):
    print("*****************")
    print(f"Answer is {" ".join(str_answer)}")
    print("*****************")
    
def main():
    str_answer = random.choice(tuple_words)
    str_hint = ["_"] * len(str_answer)
    int_wrong_guess = 0
    bln_running = True
    set_guess = set()
    
    while bln_running:
        display_man(int_wrong_guess)
        display_hint(str_hint)
        chr_guess = input("Enter a letter: ").lower() 
        
        if len(chr_guess) != 1 or not chr_guess.isalpha():
            print("Invalid Input")
            continue
        if chr_guess in set_guess:
            print(f"{chr_guess} is already guessed")
            continue
        
        set_guess.add(chr_guess)
        
        if chr_guess in str_answer:
            for i in range(len(str_answer)):
                if str_answer[i] == chr_guess:
                    str_hint[i] = chr_guess
        else:
            int_wrong_guess += 1
            
        if "_" not in str_hint:
            display_man(int_wrong_guess)
            display_answer(str_answer)
            print("YOU WIN")
            bln_running = False
        elif int_wrong_guess >= len(dict_hangman_art) - 1:
            display_man(int_wrong_guess)
            display_answer(str_answer)
            print("YOU LOSE")
            bln_running = False
            
    
if __name__ == "__main__":
    main()
