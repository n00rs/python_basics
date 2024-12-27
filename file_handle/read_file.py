# reading files in python (.txt,.json,.csv)


'''
to read file we use open function with "r"
'''

str_path = "file_handle/output_1.txt"
'''
reading .txt file
'''
try:
    with open(str_path,"r") as file:
        str = file.read()
        print(str)
except FileNotFoundError:
    print(f"{str_path} File Not Found ")
except PermissionError:
    print("Permission denied")
    
'''
reading .json file
'''
str_path = "file_handle/output_1.json"
import json

try:
    with open(str_path,"r") as file:
        dict_json = json.load(file)
        print(dict_json)
except FileNotFoundError:
    print(f"{str_path} File Not Found ")
except PermissionError:
    print("Permission denied")

'''
reading .csv file
'''
str_path = "file_handle/output_1.csv"
import csv

list_employee = []

try:
    with open(str_path,"r") as file:
        list_content = csv.reader(file)
        for line in list_content:
            list_employee.append(line)
            
        print(list_employee)
except FileNotFoundError:
    print(f"{str_path} File Not Found ")
except PermissionError:
    print("Permission denied")
    