'''Start Coding at 26/08/2017'''
" (c) 2017 Dewnith Fernando. All rights reserved."

import os

print("* DvNET Parker [version 2017.08.26] Developed by Dewnith Fernando. *")
print("* Copyright (c) 2019 Dewnith Fernando. All rights reserved.        *")
#print("Type 'help' or 'credits' for more information.")
print("")

def main():
    Userfile = open("Data/username.db", 'r')
    name = Userfile.read() 
    print("")
    ztext = input("> " + "What do you want " + name + ":>")

    if ztext == "what is your name":
        print(">", "My name is Parker. Build 071.")
        main()

    elif ztext == "c":
        print("")
        print("* ********************     CREDITS     ********************* *")
        print("*                                                            *")
        print("*                Developed by Dewnith Fernando.              *")
        print("* Special Thank to Guido Van Rosem and Wijeya Pariganaka.    *")
        print("*                                                            *")
        print("* Copyrights (c) 2017 Dewnith Fernando. All righs reserved.  *")       
        print("*                                                            *")
        print("* ********************************************************** *")
        main()

    else:
        try:
            dbf = open("Data/Database/" + ztext + ".db", "r")
            dbfr = dbf.read()
        except IOError:
            print("")
            print(">", name + ". Parker, don't know about " + ztext  +". But you can add information about " + ztext + "." )
            print("> If you want do it now type 'y' and press enter." + " Enter for none.")
            print()
            
            abdf = input("> " + name + ", What is your choice :")
            if abdf == "y":
                print(">", "Ok " + name + ".")
                print("***********" + ztext + "***********")
                ed = input("> " + name + ", Enter description of " + ztext + ":")
                obdf = open("Data/Database/" + ztext + ".db", "w+")
                obdf.write(ed)
                obdf.close()
                print(">", name + ", I stored information about " + ztext + "in my Database.")
                main()
            else:
                print(">", "Ok " + name + ".")
                main()
        else:
            print(dbfr)
            main()
try:
    Userfile = open("Data/username.db", "r")
    name = Userfile.read()
except IOError:
    print(">", "Hi, you're welcome user.")
    nuname = input("> " + "Enter your user name here :")
    os.mkdir("Data")
    os.mkdir("Data/Database")
    nufile = open("Data/username.db", "w+")
    nufile.write(nuname)
    nufile.close()
    main()
else:
    print(">", "Hi " + name + ", you're welcome to Parker")
    main()
""" Scripted Date : 2017.08.26 """