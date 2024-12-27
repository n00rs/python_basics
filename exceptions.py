'''
Exception = An event that interrupts the Flow of a program
            (ZeroDivisionError(ex : 1/0 ),TypeError,ValueError)
            1.try 2.except 3.finally
'''

try:
    int_num = int(input("Enter a number"))
    print(1/int_num)
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("Enter only numbers please...!")
except Exception:
    print("Something went wrong")
finally:
    print("Done .... !")

# bad practise
    
try:
    int_num = int(input("Enter a number"))
    print(1/int_num)
except Exception as e:
    print("Something went wrong" ,e)
finally:
    print("Done .... !")