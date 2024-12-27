'''
file detction
'''
import os

str_path = "file_handle"

if os.path.exists(str_path):
    print(f"The location '{str_path}' exists")
    
    if os.path.isfile(str_path):
        print("That's an File")
    elif os.path.isdir(str_path):
        print("That's an Folder")
        
else:
    print("The localtion doesn't Exist")