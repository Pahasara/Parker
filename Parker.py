'''Start Coding on 26/08/2017'''
" (c) 2017, 2019 Dewnith Fernando. All rights reserved."

import os

# ''' START OF CREDITS INFORMATION '''
print("* DvNET Parker [version 2019.08.26] Developed by Dewnith Fernando. *")
print("* Copyrights (c) 2017-2019 Dewnith Fernando. All rights reserved.   *")
print("")
# ''' END OF CREDITS INFORMATION '''


Robot_Name = "Parker"
LastReleaseYear = 2019
BuildVersion = "Build 0.3.0826"

#-----------------------------------------------------------------------------------------------------
# ''' MAIN CLASS --ROBOT ''''

class Robot(object):
    def __init__(self, age):
        self.age = age
        self.name = Robot_Name

    def get_age(self):
        return self.age

#-----------------------------------------------------------------------------------------------------
# ''' CLASS ATTRIBUTES --Robot.Properties ''''
Parker = Robot(1)
Parker.age = LastReleaseYear - 2017

#-----------------------------------------------------------------------------------------------------
# ''' MAIN FUNCTION --Parker.Main ''''
def main():
    Username = open("Data/Username.db", 'r')
    Username = Username.read()
    print("")
    Text = input("> " + "What do you want " + Username + ":>")

    if Text == "name":
        print("<", "My name is " + Robot_Name + ". " + BuildVersion)
        main()

    elif Text == "credits":
        print("")
        print("* ***********************     CREDITS     *********************** *")
        print("*                                                                 *")
        print("*                  Developed by Dewnith Fernando.                 *")
        print("*                                                                 *")
        print("*      Special Thank to Python Software and Wijeya Pariganaka.    *")
        print("*                                                                 *")
        print("*                     Powered by Python 3.7                       *")
        print("*                                                                 *")
        print("* Copyrights (c) 2017-2019 Dewnith Fernando. All rights reserved. *")
        print("*                                                                 *")
        print("* *************************************************************** *")
        main()

    elif Text == "age":
        print("<", "I'm " + str(Parker.age) + " Years old.")
        main()

    elif Text == "hi":
        print("<", "Hi, have a nice day " + Username + ".")
        main()

    elif Text == "hello":
        print("<", "Hello How are you " + Username + ".")
        main()

    elif Text == "del userdata":
        os.remove("Data/Username.db")
        Print("Your username file was deleted!.")
        Username = input("> " + "Enter your Username here :")
        newFile = open("Data/Username.db", "w+")
        newFile.write(Username)
        newFile.close()
        Print("Contragulations!")
        Print("Your userdata update successful!")
        main()

    elif Text == "exit":
        a = input("< " + Username + ", Please enter for exit...")
        if(a == ""):
            Print("Good bye!")
        else:
            Print("You selected none!")
            main()

    else:
        try:
            dbFile = open("Data/Database/" + Text + ".db", "r")
            dbData = dbFile.read()
        except IOError:
            print("")
            print("<",Username + ", the Parker don't know about '" + Text + "'. But you can add information about '" + Text + "'."
                  + " If you want do it now type 'y' and press enter." + " Enter for none.")
            print()

            dbFile = input("> " + Username + ", What is your choice :")
            if dbFile == "y":
                print("<", "Ok " + Username + ". You selected yes.")
                print("")
                print("< ----------------------- " + Text + " ------------------------")
                dbFile = input("> " + Username + ", Enter description of '" + Text + "':")
                dbData = open("Data/Database/" + Text + ".db", "w+")
                dbData.write(dbFile)
                dbData.close()
                print("<", Username + ", I stored information about '" + Text + "' in my Database.")
                main()
            else:
                print("<", "Ok " + Username + ". Your choice is my hapiness.")
                main()
        else:
            print("<", dbData)
            main()

#-----------------------------------------------------------------------------------------------------
# ''' Parker.Output ''''
def Print(string):
    print("<", string)
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# ''' START UP --Parker.BOOT ''''
try:
    Username = open("Data/Username.db", "r")
    Username = Username.read()
except IOError:
    print("<", "Hi, you're welcome user.")
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
    print("<", "Hi " + Username + ", you're welcome to Parker.")
    main()
#-----------------------------------------------------------------------------------------------------


""" Scripted Date  : 2017.08.26 """
""" Script Updated : 2019.08.06 """
