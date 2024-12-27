'''
if __name__ = __main__ : (this script can be imported run stand alone)
                            Function and classes in this module can be reused
                            Without excuted the code inside main block
Good Practice ( Code is modular,
                helps with readablity ,
                leaves no global variable 
                avoid unintended execution )
'''
def main():
    #program 
    pass

'''
when this used the main function will only excute 
When this scirpt is running standalone
when imported in other files it wont run the code in main block 
exp : python libraries
'''
if __name__ == "__main__":
    main()
    