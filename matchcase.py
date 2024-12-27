'''
matchcase statement(Switch) : an alternative to using many elelif statements Execute some code elif avalue
                               matches a case Benfit's cleaner and syntax is more readable
'''
def day_of_week(int_day):
    if int_day == 1:
        print("it's Sunday")
    elif int_day == 2:
        print("it's Monday")
    elif int_day == 3:
        print("it's Tuesday")
    elif int_day == 4:
        print("it's Wednesdayy")
    elif int_day == 5:
        print("it's Thursday")
    elif int_day == 6:
        print("it's Friday")
    elif int_day == 7:
        print("it's Saturday")
    else:
        print("Not a valid day")
        
day_of_week(5)

def day_of_week_match(int_day):
    match int_day:
        case 1:
            print("it's Sunday")
        case 2:
            print("it's Monday")
        case 3:
            print("it's Tuesday")
        case 4:
            print("it's Wednesdayy")
        case 5:
            print("it's Thursday")
        case 6:
            print("it's Friday")
        case 7:
            print("it's Saturday")
        case _:
            print("Not a valid day")
            
day_of_week_match(5)

def is_weekend(str_day):
    match str_day:
        case "Sunday" | "Saturday":
            return True 
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Not a valid day" 
        
print(is_weekend("Tuesday"))       
print(is_weekend("Sunday"))       