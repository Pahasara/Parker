'''Start Coding on 26/08/2017'''
" (c) 2017, 2019 Dewnith Fernando. All rights reserved."

import os

# ''' START OF CREDITS INFORMATION '''
print("* DvNET Parker [version 2019.06.15] Developed by Dewnith Fernando. *")
print("* Copyrights (c) 2017-2019 Dewnith Fernando. All rights reserved.   *")
print("")
# ''' END OF CREDITS INFORMATION '''

def main():
    Username = open("Data/Username.db", 'r')
    Username = Username.read() 
    print("")
    Text = input("> " + "What do you want " + Username + ":>")

    if Text == "what is your Username":
        print(">", "My name is Parker. Build 250.")
        main()

    elif Text == "credits":
        print("")
        print("* ***********************     CREDITS     *********************** *")
        print("*                                                                 *")
        print("*                  Developed by Dewnith Fernando.                 *")
        print("*                                                                 *")
        print("*      Special Thank to Guido Van Rosem and Wijeya Pariganaka.    *")
        print("*                                                                 *")
        print("* Copyrights (c) 2017-2019 Dewnith Fernando. All righs reserved.  *")       
        print("*                                                                 *")
        print("* *************************************************************** *")
        main()

    else:
        try:
            dbFile = open("Data/Database/" + Text + ".db", "r")
            dbData = dbFile.read()
        except IOError:
            print("")
            print(">", Username + ", the Parker don't know about '" + Text  +"'. But you can add information about " + Text + "." )
            print("> If you want do it now type 'y' and press enter." + " Enter for none.")
            print()
            
            dbFile = input("> " + Username + ", What is your choice :")
            if dbFile == "y":
                print(">", "Ok " + Username + ". You selected yes.")
                print("")
                print("> ----------------------- " + Text + " ------------------------")
                dbFile = input("> " + Username + ", Enter description of '" + Text + "':")
                dbData = open("Data/Database/" + Text + ".db", "w+")
                dbData.write(dbFile)
                dbData.close()
                print(">", Username + ", I stored information about '" + Text + "' in my Database.")
                main()
            else:
                print(">", "Ok " + Username + ". Your choice is my hapiness.")
                main()
        else:
            print(">",dbData)
            main()
try:
    Username = open("Data/Username.db", "r")
    Username = Username.read()
except IOError:
    print(">", "Hi, you're welcome user.")
    Username = input("> " + "Enter your Username here :")
    os.mkdir("Data")
    os.mkdir("Data/Database")
    newFile = open("Data/Username.db", "w+")
    newFile.write(Username)
    newFile.close()
    print("")
    print("* Type 'help' or 'credits' for more information.")
    main()
else:
    print(">", "Hi " + Username + ", you're welcome to Parker.")
    main()

""" Scripted Date  : 2017.08.26 """
""" Script Updated : 2019.06.15 """