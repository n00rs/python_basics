'''
multithreading : to perform multiple task concurrenctly (multiple task)
                 good for I/o bound tasks like reading file or fetching data
'''
import threading
import time

# takes 8s to complete
def walkdog(str_first_name,str_last_name):
    time.sleep(8)
    print(f"Walking the dog {str_first_name} {str_last_name}")
    
# takes 2s to complete 
def take_out_trash():
    time.sleep(2)
    print("Taken the trash")

#takes 5s to complete 
def get_mail():
    time.sleep(5)
    print("get the mail")
    
    
    
    
'''
the whole process take 15s to complete
'''    
# walkdog() 
# take_out_trash() 
# get_mail() 


'''
using multi threading to run them con currently
here the whole process takes max of 8s
'''

# chore1 = threading.Thread(target=walkdog)
# to pass arguments to child use arg key and pass an tuple
chore1 = threading.Thread(target=walkdog,args=("scoobee","Doo"))

chore1.start()
chore2 = threading.Thread(target=take_out_trash)
chore2.start()
chore3 = threading.Thread(target=get_mail)
chore3.start()

# to wait unit ALL are executed 
chore1.join()
chore2.join()
chore3.join()

print("Completed") #this will printed first if we dont use join