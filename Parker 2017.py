'''Start Coding on 26/08/2017'''
" (c) 2017 Dewnith Fernando. All rights reserved."

print("DvNET Parker [version 0.1] First Release 2017.08.26")
print("Copyright (c) 2017 Dewnith Fernando. All rights reserved.")
print("")

def ZMAIN():
    Userfile = open("Data/username.zdb", 'r')
    name = Userfile.read() 
    print("")
    ztext = input("What do you want " + name + ":>")

    if ztext == "what is your name":
        print("My name is Parker. Version 0.1.")
        ZMAIN()

    elif ztext == "credits":
        print("")
        print("+------------------------- CREDITS --------------------------+")
        print("+                                                            +")
        print("+                     *  Developer  *                        +")
        print("+                   M.P.Dewnith Fernando.                    +")
        print("+                                                            +")
        print("+                   *  Special Thank  *                      +")
        print("+                     Guido Van Rosem                        +")
        print("+                 Wijeya Pariganaka Newspaper.               +") 
        print("+                                                            +")
        print("+ Copyrights (c) 2017 Dewnith Fernando. All righs reserved.  +")       
        print("+------------------------------------------------------------+")
        ZMAIN()

    else:
        try:
            dbf = open("Data/" + ztext + ".zdb", "r")
            dbfr = dbf.read()
        except IOError:
            print("")
            print(name + ". Parker, don't know about " + ztext  +". But you can add information about " + ztext + "." )
            print("If you want do it now type 'y' and press enter." + " Enter for none.")
            print("")
            
            abdf = input(name + ", What is your choice :")
            if abdf == "y":
                print(">", "Ok " + name + ".")
                print("----------" + ztext + "----------")
                ed = input("> " + name + ", Enter description of " + ztext + ":")
                obdf = open("Data/" + ztext + ".zdb", "w+")
                obdf.write(ed)
                obdf.close()
                print(name + ", I saved information about " + ztext + " in my Database.")
                ZMAIN()
            else:
                print("Ok " + name + ".")
                ZMAIN()
        else:
            print(dbfr)
            ZMAIN()
try:
    Userfile = open("Data/username.zdb", "r")
    name = Userfile.read()
except IOError:
    print("Hi, you're welcome user.")
    nuname = input("Enter your user name here :")  
    nufile = open("Data/username.zdb", "w+")
    nufile.write(nuname)
    nufile.close()
    ZMAIN()
else:
    print("Hi " + name + ", you're welcome")
    ZMAIN()

""" Developer : M.P.Dewnith Fernando."""
""" Scripted Date  : 2017.08.26 """