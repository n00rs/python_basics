'''
for loops = execute a block of code a fixed number of times 
you can iterrate over a range ,string, sequence etc..
'''

for i in range(0,11):
    print(i)
    
for i in reversed(range(0,11,2)):
    print(i)
print("Happy new year")

str_cc_num = "1234-6542-9874-9633"

for i in str_cc_num:
    print(i)
    
# ex for continue
for i in str_cc_num:
    if i == "-":
        continue
    else:
        print(i)
        
# ex for break
for i in str_cc_num:
    if i == "-":
        break
    else:
        print(i)

'''
Count timer in python
'''
        
import time

int_time = int(input("Enter the time in second's :"))

for i in range(int_time,0,-1):
    int_seconds = i % 60
    int_minutes = int(i/60) % 60
    int_hours = int(i/3600)
    print(f"{int_hours:02}:{int_minutes:02}:{int_seconds:02}")
    time.sleep(1)

print("TIME'S UP")

'''
nested loop = A loop within another loop (outer , inner )
                outer loop:
                    inner loop:
'''
int_rows = int(input("Enter the no of rows: "))
int_columns = int(input("Enter the no of columns: "))
symbol = input("Enter the an symbol to print: ")

for i in range(int_rows):
     for j in range(int_columns):
         print(symbol,end="")
     print()
