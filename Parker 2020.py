''' Start Coding on 26/08/2017 '''
''' (c) 2017, 2020 Dewnith Fernando. All rights reserved. '''

import os
import random

Robot_Name = "Parker"
ReleaseYear = 2020
BuildVersion = "0.4.0118"

# ''' START OF CREDITS INFORMATION '''
print("* DvNET " + Robot_Name + " [version " + BuildVersion + "] Developed by Dewnith Fernando.  *")
print("* Copyrights (c) 2017-" + str(ReleaseYear) + " Dewnith Fernando. All rights reserved. *")
print()
print("******* THE LAST RELEASE OF PARKER BY DvNET [Dewnith Fernando] *******")
print()
# ''' END OF CREDITS INFORMATION '''

# -----------------------------------------------------------------------------------------------------
# ''' MAIN CLASS --ROBOT ''''
class Robot(object):
    def __init__(self, age):
        self.age = age
        self.name = Robot_Name
        self._temp = ""
        self._userFile = "Data/UserDB.db"

    def get_age(self):
        Parker.age = ReleaseYear - 2017
        return Parker.age


# -----------------------------------------------------------------------------------------------------
# ''' CLASS ATTRIBUTES --Robot.Properties ''''
Parker = Robot(1)


# -----------------------------------------------------------------------------------------------------
# ''' MAIN FUNCTION --Parker.Main ''''
def main():
    Username = open(Parker._userFile, 'r')
    Username = Username.read()

    print("")
    Text = input(":> ")

    if Text == "name":
        Print("My name is " + Robot_Name + ". Build " + BuildVersion)
        main()

    elif Text == "credits":
        print("")
        print("* ***********************     CREDITS     *********************** *")
        print("*                                                                 *")
        print("*                  Developed by Dewnith Fernando.                 *")
        print("*                                                                 *")
        print("*      Special Thank to Guido Van Rosum and Wijeya Pariganaka.    *")
        print("*                                                                 *")
        print("*                     Powered by Python 3.8                       *")
        print("*                                                                 *")
        print("* Copyrights (c) 2017-" + str(ReleaseYear) + " Dewnith Fernando. All rights reserved. *")
        print("*                                                                 *")
        print("* *************************************************************** *")
        main()

    elif Text == "age":
        Print("I'm " + str(Parker.get_age()) + " Years old.")
        main()

    elif Text == "hi":
        Print("Hi, have a nice day " + Username + ".")
        main()

    elif Text == "":
        if Parker._temp == "0":
            Print("Why are you enter none?")
            Parker._temp = ""
        else:
            Print("It's a free text!")
            Parker._temp = "0"
        main()

    elif Text == "radd":
        addRNDTXT()
        main()

    elif Text == "rdel":
        remRNDTXT()
        main()

    elif Text == "add":
        sDATA("add", Text)
        main()

    elif Text == "help":
        help()
        main()

    elif Text == "change username":
        os.remove(Parker._userFile)
        Print("Your username file was deleted!.")
        Username = input(":> " + "Enter a new username here: ")
        newFile = open(Parker._userFile, "w+")
        newFile.write(Username)
        newFile.close()
        Print("Congratulations!")
        Print("Your username update successful!")
        main()

    elif Text == "exit":
        exitPROG()

    else:
        sDATA("get", Text)
        main()


# -----------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------
# ''' METHODS '''

def Print(string):
    print("<:", string)


def sDATA(str, txt):
    dbIN = open("Data/Database0.db", "r+")
    dbOUT = open("Data/Database1.db", "r+")
    dataIN = dbIN.read()
    listIN = list(dataIN.split(";"))
    dataOUT = dbOUT.read()
    listOUT = list(dataOUT.split(";"))

    if str == "get":
        try:
            idIN = listIN.index(txt)
        except:
            dbIN.close()
            dbOUT.close()
            Print(getRNDTXT())
        else:
            DATA = listOUT[idIN]
            Print(DATA)
            dbIN.close()
            dbOUT.close()

    elif str == "add":
        Print("******   -ADDING DATA-    ******")
        _userIN = input(":> " + "Enter a title: ")
        # Database0 --save title
        dbIN = open("Data/Database0.db", "r+")
        dataIN = dbIN.read() + ";" + _userIN
        dbIN.close()
        os.remove("Data/Database0.db")
        dbIN = open("Data/Database0.db", "w+")
        dbIN.write(dataIN)
        dbIN.close()
        # Database1 --save data
        print()
        _userOUT = input(":> " + "Enter about '" + _userIN.upper() + "': ")
        dbOUT = open("Data/Database1.db", "r+")
        dataOUT = dbOUT.read() + ";" + _userOUT
        dbOUT.close()
        os.remove("Data/Database1.db")
        dbOUT = open("Data/Database1.db", "w+")
        dbOUT.write(dataOUT)
        dbOUT.close()
        Print("Added about '" + _userIN.upper() + "' in my database.")


def getRNDTXT():
    RandFile = open("Data/RandomDB.db", "r")
    RandData = RandFile.read()
    RandData = list(RandData.split(";"))
    RNDTXT = random.choice(RandData)
    RandFile.close()
    while RNDTXT == Parker._temp:
        RNDTXT = random.choice(RandData)
    else:
        Parker._temp = RNDTXT
    return RNDTXT


def addRNDTXT():
    _inputRndText = input("<: Enter a random text:> ")
    RandFile = open("Data/RandomDB.db", "r+")
    RandData = RandFile.read() + ";" + _inputRndText
    RandFile.close()
    os.remove("Data/RandomDB.db")
    RandFile = open("Data/RandomDB.db", "w+")
    RandFile.write(RandData)
    Print("Added about '" + _inputRndText.upper() + "' in RandomDB.")


def remRNDTXT():
    strem = input("<: Enter the text to delete:> ")
    RandFile = open("Data/RandomDB.db", "r+")
    RandData = RandFile.read()
    RandData = list(RandData.split(";"))
    try:
        RandData = RandData.remove(strem)
        RandFile.write(str(RandData))
        RandFile.close()
        Print("'" + strem.uppuer + "' was deleted!")
    except:
        Print("'" + strem.uppuer + "' is not found in your RandomDB!")

def help():
    print()
    print("* ----------------------------------------------- *")
    print()
    Print("(c)2017-2020 Dewnith Fernando. All rights reserved.")
    print()
    Print("Parker was created on 26 August 2017 by Dewnith Fernando [DvNET]")
    Print("This update was released on 18 January of 2020 by own me. [DvNET]")
    Print("I won't be able to do another update of Parker.")
    Print("So this is the last update of my first computer program.")
    Print("I have been updating for 3 years since then...")
    print()
    Print("* ------------------ COMMANDS ------------------- *")
    print()
    Print("  radd : Add random words")
    Print("  rdel : Delete a random word")
    Print("  add  : Add data to the 'Database'")
    Print("  change username : Change your username")
    Print("  exit : Exit from the program")
    print()
    print("* ----------------------------------------------- *")
    print()

def exitPROG():
    sure = input(":> " + Username + ", Please enter for exit...")
    if (sure == ""):
        Print("Good bye!")
    else:
        Print("You selected none!")
        main()


# -----------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------
# ''' START UP --Parker.BOOT ''''
try:
    UserFile = open(Parker._userFile, "r")
except IOError:
    Print("Hi, you're welcome user.")
    Username = input("> " + "Enter your Username here:> ")
    os.mkdir("Data")
    UserFile = open(Parker._userFile, "w+")
    UserFile.write(Username)
    UserFile.close()
    newRandFile = open("Data/RandomDB.db", "w+")
    newRandFile.close()
    newDBFile0 = open("Data/Database0.db", "w+")
    newDBFile0.close()
    newDBFile1 = open("Data/Database1.db", "w+")
    newDBFile1.close()
    print("")
    main()
else:
    Username = UserFile.read()
    print("* Type 'help' or 'credits' for more information.")
    print()
    Print("Hi " + Username + ", you're welcome to Parker.")
    main()
# -----------------------------------------------------------------------------------------------------


""" Scripted Date  : 2017.08.26 """
""" Script Updated : 2020.01.18 """