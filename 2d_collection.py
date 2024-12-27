'''
2d Lists : 
   a list that contain lists -> [list1,list2,list3,list4]
'''
list_fruits = ["apple","orange","mango","anar"]
list_vegtales = ["carrot","tomato","potato"]
list_meats = ["chicken","pig","fish"]

list_groceries = [list_fruits,list_vegtales,list_meats]

print(list_groceries[1])

for collection in list_groceries:
    for food in collection:
        print(food,end=" ")
    
'''
key pad dialer
'''
tuple_num_pad = ((1,2,3),
                 (4,5,6),
                 (7,8,9),
                 ("*",0,"#") 
                 )

for row in tuple_num_pad:
    for num in row:
        print(num,end=" ")
    print()
    
'''
python quiz game
'''

tuple_question = ("How many elements are there in periodic table ?: ",
                  "Which animal lays largest egg ?: ",
                  "What is the most abundant gas in Earth's atmosphere ?: ",
                  "How many bones are there in human body ?: ",
                  "Which planet in the solar system is hottest ?:"
                  )
tuple_options = (("A. 116","B. 117","C. 118","D. 119"),
                 ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
                 ("A. Nitrogen","B. Oxygen","C. Carbon-dioxide","D. Hydrogen"),
                 ("A. 206","B. 207","C. 208","D. 209"),
                 ("A. Mercury","B. Venus","C. Mars","D. Earth"))
tuple_answers = ("C","D","A","A","B")
list_gueses=[]
dbl_score = 0
int_question_num = 0
# looping through list of question
for question in tuple_question:
    print("=================")
    print(question)
    # looping through list of options
    for option in tuple_options:
        print(option)
    # getting user answer
    str_answer = input("Enter (A,B,C,D): ").upper()
    list_gueses.append(str_answer)
    # if answer is correct then add score
    if str_answer == tuple_answers[int_question_num]:
        print("CORRECT")
        dbl_score +=1
    else:
        print("INCORRECT")
        print(f"{tuple_answers[int_question_num]} is the correct answer ")
    # add index number
    int_question_num += 1
    
print("answers: ",end=" ")
for answer in tuple_answers:
    print(answer,end=" ")
print()

print("guess: ",end=" ")
for guess in list_gueses:
    print(guess,end=" ")
print()
# calculating score
dbl_score = int(dbl_score / len(tuple_question) * 100)

print(f"Your Score is: {dbl_score} %")