''' Started Coding on 26/08/2017 '''
''' (c) 2017, 2021 Dewnith Fernando. All rights reserved. '''

import win32con, win32api, os, random, time, datetime, stdiomask
from cryptography.fernet import Fernet

Robot_Name = "Parker"
ReleaseYear = 2021
ReleaseMonth = 8
ReleaseDate = 26
BuildVersion = "1.0.2108.824"

# ''' START OF CREDITS INFORMATION '''
print("* DvNET " + Robot_Name + " [version " + BuildVersion + "] Developed by Dewnith Fernando.")
time.sleep(0.1)
print("* Copyrights (c) 2017-" + str(ReleaseYear) + " Dewnith Fernando. All rights reserved.\n")
time.sleep(2)
# ''' END OF CREDITS INFORMATION '''

# -----------------------------------------------------------------------------------------------------
# ''' MAIN CLASS --ROBOT ''''
class Robot(object):
    def __init__(self, age):
        self.age = age
        self.name = Robot_Name
        self._temp = ""
        self._userFile = "Data/Database1.db"

    def get_age(self):
        year = datetime.date.today().year
        month = datetime.date.today().month
        date = datetime.date.today().day
        if(year>ReleaseYear):
            years = year - 2017
            if(month >= ReleaseMonth):
                if(date >= ReleaseDate):
                    self.age = years
        else:
            self.age = 5
        return self.age
# -----------------------------------------------------------------------------------------------------
# ''' CLASS ATTRIBUTES --Robot.Properties ''''
Parker = Robot(1)
# -----------------------------------------------------------------------------------------------------
# ''' MAIN FUNCTION --Parker.Main ''''
def main():
    print("")
    time.sleep(0.1)
    Text = input(":> ")

    if Text == "name":
        Print("My name is " + Robot_Name + ". Build " + BuildVersion)
        main()

    elif Text == "credits":
        Credits()
        main()

    elif Text == "age":
        Print("I'm " + str(Parker.get_age()) + " years old.")
        main()

    elif Text == "":
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
    
    elif Text == "del":
        sDATA("delete",Text)
        main()
        
    elif Text == "update":
        sDATA("update",Text)
        main()

    elif Text == "help":
        help()
        main()

    elif Text == "username":
        global y,d
        y=''
        global Username
        CONFIRM()
        if(d=='s'):
            Username = input(":> " + "Enter a new username: ")
            Password = readUINFO('pass')
            saveDATA("*f#hj86go*",enc(Username))
            saveDATA("*f#hj96go*",enc(Password))
            Password = ""
            PrintX("USERNAME UPDATED\n")
            d=''
            main()
        else:
            main()
    elif Text == "password":
        y=''
        CONFIRM()
        if(d=='s'):
            Password = stdiomask.getpass(prompt=':> Enter a new password: ')
            Username = readUINFO()
            saveDATA("*f#hj86go*",enc(Username))
            saveDATA("*f#hj96go*",enc(Password))
            Password = ""
            PrintX("PASSWORD UPDATED\n")
            d=''
            main()
        else:
            main()

    elif Text == "exit":
        exitPROG()
    
    elif Text == "rdb":
        viewRDB()
        main()
    
    elif Text == "enc":
        Encrypt()
        main()
        
    elif Text == "dec":
        Decrypt()
        main()

    elif Text == "lout":
        PrintX("LOGGED OUT!\n")
        x=''
        logIN()
        
    elif Text == "activate":
        Activate()
        main()

    else:
        sDATA("get", Text)
        main()

# -----------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------
# ''' METHODS '''

# -- DEFINE PRINT METHOD --
def Print(string, mark="<: "):
    string = string.replace("_USER", Username)
    print(mark,end=string)

# -- DEFINE SYSTEM.OUT METHOD --
def PrintX(string, mark="<: SYSTEM: "):
    string = string.replace("_USER", Username)
    print(mark, end=string)

# -- DEFINE SYSTEM.ERROR METHOD --
def PrintZ(string, mark="<: ERROR: "):
    string = string.replace("_USER", Username)
    print(mark,end=string)

# -- ADD/RETURN DATA --
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
            Print(getRNDTXT()+"\n")
        else:
            DATA = listOUT[idIN]
            Print(DATA+"\n")
            dbIN.close()
            dbOUT.close()
            
    elif str == "delete":
        try:
            _userIN = input(":> Enter the title : ")
            if(_userIN==""):
                PrintZ("ENTERED NONE!\n")
                main()
            else:            
                idIN = listIN.index(_userIN)
                listOUT.pop(idIN)
                dataIN = dataIN.replace(";"+_userIN, "")
                dataOUT = listToString(listOUT)
        except:            
            PrintZ("'{}' {}".format(_userIN.upper() ,"DOESN'T EXIST!\n"))
        else:
            # Database0 --delete title
            dbIN = open("Data/Database0.db", "w+")
            dbIN.write(dataIN)
            dbIN.close()
            # Database1 --delete data
            dbOUT = open("Data/Database1.db", "w+")
            dbOUT.write(dataOUT)
            dbOUT.close()
            PrintX("OPERATION SUCCESS\n")  
            
    elif str == "update":
        try:
            _userIN = input(":> Enter the title : ")
            if(_userIN==""):
                PrintZ("ENTERED NONE!\n")
                main()
            else:            
                idIN = listIN.index(_userIN)
        except:            
            PrintZ("'{}' {}".format(_userIN.upper() ,"DOESN'T EXIST!\n"))
        else:
            _userOUT = input(":> " + "Enter about '" + _userIN.upper() + "': ")
            if(_userOUT==""):
                PrintZ("ENTERED NONE!\n")
                dbIN.close()
                dbOUT.close()
                main()
            else:            
                dbIN.close()
                listOUT[idIN] = _userOUT
                dataOUT = listToString(listOUT)
                # Database1 --update data
                dbOUT = open("Data/Database1.db", "w+")
                dbOUT.write(dataOUT)
                dbOUT.close()
                PrintX("UPDATE SUCCESS\n") 

    elif str == "add":
        Print("------------------------------------------------------\n")
        print("                   ***  ADDING DATA  ***")
        Print("------------------------------------------------------\n")
        _userIN = input(":> " + "Enter the title: ")
        if(_userIN==""):
            PrintZ("ENTERED NONE!\n")
            dbIN.close()
            dbOUT.close()
            main()        
        elif(getDATA(_userIN)!=""):
            PrintZ("Definition about '" + _userIN + "' already saved in Parker's database.\n")
            Print("HINT: But you can use 'update' command to update previous definition about '" +_userIN + "'\n")        
            time.sleep(0.1)
            Print("------------------------------------------------------\n")
            main()
        else:        
            _userOUT = input(":> " + "Enter about '" + _userIN.upper() + "': ")
            if(_userOUT==""):
                PrintZ("ENTERED NONE!\n")
                dbIN.close()
                dbOUT.close()
                main()
            else:           
                # Database0 --save title
                dbIN = open("Data/Database0.db", "r+")
                dataIN = dbIN.read() + ";" + _userIN
                dbIN.close()
                os.remove("Data/Database0.db")
                dbIN = open("Data/Database0.db", "w+")
                dbIN.write(dataIN)
                dbIN.close()
                # Database1 --save data             
                dbOUT = open("Data/Database1.db", "r+")
                dataOUT = dbOUT.read() + ";" + _userOUT
                dbOUT.close()
                os.remove("Data/Database1.db")
                dbOUT = open("Data/Database1.db", "w+")
                dbOUT.write(dataOUT)
                dbOUT.close()
                PrintX("DATABASE UPDATED\n")
                Print("------------------------------------------------------\n") 


# -- GET RANDOM TEXT --
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
        ROUT = str(RNDTXT)       
        ROUT = ROUT.replace("_USER", Username)
    return ROUT


# -- ADD RANDOM TEXT --
def addRNDTXT():
    _inputRndText = input(":> Enter a random text: ")
    if(_inputRndText==""):
        PrintZ("ENTERED NONE!\n")
    else:
        RandFile = open("Data/RandomDB.db", "r+")
        RandData = RandFile.read() + ";" + _inputRndText
        RandFile.close()
        os.remove("Data/RandomDB.db")
        RandFile = open("Data/RandomDB.db", "w+")
        RandFile.write(RandData)
        RandFile.close()
        PrintX("DATABASE UPDATED\n")

# -- REMOVE RANDOM TEXT --
def remRNDTXT():
    strem = input("<: Enter the text to delete:> ")
    if(strem==""):
        PrintZ("ENTERED NONE!\n")
    else:
        RandFile = open("Data/RandomDB.db", "r+")
        RandData = RandFile.read()
        RandFile.close()
        try:
            RandFile = open("Data/RandomDB.db", "w+")
            RandData = RandData.replace(";" + strem, "")
            RandFile.write(RandData)
            RandFile.close()
            PrintX("'" + strem.upper() + "' DELETED!\n")
        except:
            PrintZ("'" + strem.upper() + "' DOESN'T EXIST!\n")

# -- HELP/ABOUT --
def help():
    print()
    Print("------------------------------------------------------\n")
    print("                   ***  INSTRUCTIONS  *** ")
    time.sleep(0.2)
    Print("------------------------------------------------------\n")
    print("<: * Use '_USER' in definitions to display username.")
    Print("------------------------------------------------------\n\n")
    time.sleep(0.8)
    Print("------------------------------------------------------\n")
    print("                    ***  COMMANDS  ****")
    time.sleep(0.2)
    Print("------------------------------------------------------\n")
    Print("  add            Add data to the 'Database'\n")
    Print("  activate       Activate the program'\n")    
    Print("  dec            Decrypt text\n")
    Print("  del            Delete a definition\n")
    Print("  enc            Encrypt text\n")  
    Print("  exit           Exit from the program\n")
    Print("  lout           Log out from Parker\n")
    Print("  password       Change my password\n")
    Print("  radd           Update random word database\n")
    Print("  rdel           Delete a random word\n")    
    Print("  rdb            View random database\n")
    Print("  update         Update a definition\n")
    Print("  username       Change my username\n")
    Print("------------------------------------------------------\n")

# -- EXIT PROGRAM --
def exitPROG():
    print("<: " + Username + ", Please wait for exit", end="")
    time.sleep(0.1)
    print(".", end="")
    time.sleep(0.1)
    print(".")
    time.sleep(0.8)

#-- VIEW RDB --
def viewRDB():
    RandFile = open("Data/RandomDB.db", "r")
    RandData = RandFile.read()
    RandFile.close()
    RandData = list(RandData.split(";"))
    Print("------------------------------------------------------\n")
    print("                   ***  RANDOM DATA  ***")
    Print("------------------------------------------------------\n")
    for i in RandData:
        print("<: " + i)
        RDI= len(RandData)-1
        if(i== RandData[RDI]):
            Print("------------------------------------------------------\n")
            break
            
#-- ENCRYPT --
def enc(message,key='X4svTU06jsOyfMIkbh5HOk841l51iyWUxcc4F4WAqNA='):
    fernet = Fernet(key)
    encMessage = fernet.encrypt(bytes(message,'utf-8'))
    return encMessage.decode()
    
#-- DECRYPT --
def dec(message,key='X4svTU06jsOyfMIkbh5HOk841l51iyWUxcc4F4WAqNA='):
    fernet = Fernet(key)
    decMessage = fernet.decrypt(bytes(message,'utf-8')).decode()
    return decMessage

#-- LOGIN --
def logIN(tp=''):
    global x
    if(x==""):
        print()
        Print("------------------------------------------------------\n")
        print("                     ***  LOG IN  *** ")
        Print("------------------------------------------------------\n")
        x="log"
        logIN()
    else:
        if(tp == ''):     
            uname = input(":> Enter your username: ")
            if(uname == readUINFO()):
                logIN('pass')
            else:
                PrintZ('WRONG USERNAME!\n')
                time.sleep(0.5)
                logIN()
        else:
            upass = stdiomask.getpass(prompt=":> Enter your password: ")
            if(upass == readUINFO('pass')):
                PrintX('LOGIN SUCCESS\n')
                Print("------------------------------------------------------\n\n")
                time.sleep(0.5)
                Print("Hi, " + Username + ". You're welcome to Parker.\n")
                time.sleep(0.1)
                main()
            else:
                PrintZ('WRONG PASSWORD!\n')
                time.sleep(0.5)
                logIN('pass')
#-- READ USER INFO --
def readUINFO(uType=''):
    global Username 
    if(uType == "pass"):
        upass= dec(getDATA("*f#hj96go*"))
        return upass
    else:
        uname = dec(getDATA("*f#hj86go*"))
        return uname       
    Username = uname
    
#-- CONFIRM --
def CONFIRM(Type=''):
    global y
    global x
    global d
    if(y!="c"):
        Print("------------------------------------------------------\n")
        print("                     *** CONFIRM  *** ")
        Print("------------------------------------------------------\n")
        time.sleep(0.2)
        y='c'
        CONFIRM()
    else:
        uname = input(":> Enter your current username: ")
        if(uname == readUINFO()):
            upass = stdiomask.getpass(prompt=":> Enter your current password: ")
            if(upass == readUINFO('pass')):
                PrintX('CONFIRM SUCCESS\n')
                time.sleep(0.2)
                d='s'
            else:
                PrintZ('CONFIRM FAILED!\n')
                time.sleep(0.5)
                d='f'
        else:
            PrintZ('CONFIRM FAILED!\n')
            time.sleep(0.5)
            d='f'
        
#-- LIST 2 STR -- 
def listToString(s):    
    str1 = ";" 
    return (str1.join(s))

#-- PRIVATE KEY --
def getKey(t=''):
    global pkey   
    if(t==''):
        print()
        pkey = stdiomask.getpass(prompt=":> Enter a key to encrypt: ")
        if(pkey==""):
            PrintZ("ENTERED NONE!\n")
            main()
        elif(len(pkey)==8):
            if(pkey.isalnum()==False):
                Print("SYMBOLS ARE NOT VALID!\n")
                time.sleep(0.5)
                getKey()
            Print("------------------------------------------------------\n")
            Print("HINT: You should backup this key somewhere safe.\n")
            Print("HINT: This key is necessary to decrypt cipher text.\n")
            time.sleep(0.7)
        else:
            PrintZ("YOU ENTERED A WRONG KEY!\n")
            time.sleep(0.5)
            getKey()
    else:
        Print("HINT: Decryption key must be 8 characters. \n")
        Print("HINT: This key is case sensitive\n")
        Print("------------------------------------------------------\n")
        time.sleep(0.7)
        print()
        pkey = stdiomask.getpass(prompt=":> Enter key to decrypt: ")
        if(pkey==""):
            PrintZ("ENTERED NONE!\n")
            main()
        if(len(pkey)!=8):
            PrintZ("YOU ENTERED A WRONG KEY!\n")
            time.sleep(0.6)
            getKey('dec')
            
#-- ENCRYPT --
def Encrypt():
    global pkey
    Print("------------------------------------------------------\n")
    print("                    ***  ENCRYPTER  ***")
    Print("------------------------------------------------------\n")
    Print("HINT: ENCRYPTION KEY MUST BE 8 CHARACTERS.\n")
    Print("HINT: This key is case sensitive\n")
    Print("HINT: Only A-Z, a-z, 0-9 are valid characters.\n")
    Print("------------------------------------------------------\n")
    time.sleep(0.8)
    text = input(":> Enter plain text: ")
    if(text==""):
            PrintZ("ENTERED NONE!\n")
            main()
    getKey()
    key = 'Z4s9xccipU06jnOy' + pkey+ 'Ok841l51iyWUF4WAqNA='
    Print("------------------------------------------------------\n")
    print('{} {}'.format('<: Cipher text:', enc(text,key)))
    Print("------------------------------------------------------\n")

#-- DECRYPT --
def Decrypt(t=''):
    global pkey
    global text
    if(t==''):
        Print("------------------------------------------------------\n")
        print("                   ***  DECRYPTER  ***")
        Print("------------------------------------------------------\n")
        text = input(":> Enter cipher text: ")  
        Print("------------------------------------------------------\n")
        if(text==""):
            PrintZ("ENTERED NONE!\n")
            main()
        Decrypt('1')        
    else:
        getKey('dec')
        key = 'Z4s9xccipU06jnOy' + pkey + 'Ok841l51iyWUF4WAqNA='
        try:
            plain_text = dec(text,key)
            Print("------------------------------------------------------\n")
            print('{} {}'.format('<: Plain text:', plain_text))
            Print("------------------------------------------------------\n")
            text = ''
        except:
            PrintZ("KEY DOESN'T MATCH!\n")
            time.sleep(0.5)
            Decrypt('1')

#-- CREDITS --      
def Credits():
    print()
    Print("------------------------------------------------------\n")
    print("                     ***  CREDITS  ***                   ")
    Print("------------------------------------------------------\n")
    time.sleep(0.1)
    Print("       DEVELOPER            DvNET\n")
    Print("       IO TESTER            ANOCLYDER\n")
    Print("       SPECIAL THANK        Pariganaka\n")
    Print("------------------------------------------------------\n")
    time.sleep(0.2)
    print("<: (c) 2017-" + str(ReleaseYear) + " Dewnith Fernando. All rights reserved.")
    time.sleep(0.1)
    Print("------------------------------------------------------\n")
    time.sleep(0.6)

#-- GET DATA --
def getDATA(txt):
    dbIN = open("Data/Database0.db", "r+")
    dbOUT = open("Data/Database1.db", "r+")
    dataIN = dbIN.read()
    listIN = list(dataIN.split(";"))
    dataOUT = dbOUT.read()
    listOUT = list(dataOUT.split(";"))
    try:
        idIN = listIN.index(txt)
    except:           
        return ''
    else:
        DATA = listOUT[idIN]       
        dbIN.close()
        dbOUT.close()
        return DATA

#-- UPDATE DATA --
def saveDATA(_in,data):
    try:
        dbIN = open("Data/Database0.db", "r+")
        dbOUT = open("Data/Database1.db", "r+")
        dataIN = dbIN.read()
        listIN = list(dataIN.split(";"))
        dataOUT = dbOUT.read()
        listOUT = list(dataOUT.split(";"))
        idIN = listIN.index(_in)
        listOUT[idIN] = data 
        dataOUT = listToString(listOUT)
    except:   
        dbIN.close()
        dbOUT.close()
    else:
        # Database1 --delete data
        dbIN.close()
        dbOUT = open("Data/Database1.db", "w+")
        dbOUT.write(dataOUT)
        dbOUT.close()   

#-- CHECK LICENSE --
def checkVALID():
    license = "Dv43T-S41LK-H3L1O-W041D"
    if(getDATA('*f#hj76go*')==license):
        logIN()
    else:
        year0 = int(dec(getDATA('*f#hl76go*')))
        year = datetime.date.today().year  
        month0 = int(dec(getDATA('*f#hk76go*')))
        month = datetime.date.today().month                    
        day0 = int(dec(getDATA('*f#hd76go*')))
        day = datetime.date.today().day 
        dayz = int(dec(getDATA('*f#hd75go*')))
        if(month0!=12):
            if(year0==year):
                if(month0==month-1):
                    d=30-day0
                    d=30-d-day
                    if d>0: Remain(d,dayz)        
                    else: Expire(dayz)
                else:
                    d=day-day0
                    d=30-d
                    Remain(d,dayz)
            else:
                Expire(d)
        else:
            if(year0==year-1):
                if(month==1):
                    d=30-day0
                    d=30-d-day
                    if d>0: Remain(d,dayz)        
                    else: Expire(dayz)
                else:
                    if(month0==month):
                        d=day-day0
                        d=30-d
                        Remain(d,dayz)
                    else:
                        Expire(dayz)
            else:
                Expire(dayz)           
            
#-- REMAIN LICENSE --
def Remain(d,dayz): 
    if(d==30 and dayz==30):
        print()              
        Print("{} {} {}".format("LICENSE: REMAINING", dayz,"DAYS.\n")) 
        time.sleep(2)
        dayz = enc(str(dayz))
        saveDATA('*f#hd75go*',dayz)
        logIN()  
    elif(d<=dayz and d<=30 and dayz<=30 and d>=0):
        if(d==1):            
            print()
            Print("YOUR LICENSE WILL EXPIRE TOMORROW.\n") 
            saveDATA('*f#hd75go*',d)
            time.sleep(2)
            logIN() 
        else:
            print()              
            Print("{} {} {}".format("LICENSE: REMAINING", d,"DAYS.\n")) 
            time.sleep(2)
            d = enc(str(d))
            saveDATA('*f#hd75go*',d)
            logIN()            
    else: 
        Expire(dayz)
            
#-- EXPIRE --
def Expire(dayz):
    print()
    dayz=dayz-2
    saveDATA('*f#hd75go*',dayz)
    PrintX("YOUR LICENSE EXPIRED!\n\n")
    time.sleep(2)
    EXactivate()
    
#-- EXPIRED LICENSE --
def EXactivate():
    license = stdiomask.getpass(prompt=":> Enter license key to activate: ")
    if(license=="Dv43T-S41LK-H3L1O-W041D"):               
        dbOUT = open("Data/Database1.db", "r+")
        dataOUT = dbOUT.read()
        dbOUT.close()
        os.remove("Data/Database1.db")
        dataOUT = dataOUT.replace("*f#hj76go*","Dv43T-S41LK-H3L1O-W041D")
        dbOUT = open("Data/Database1.db", "w+")
        dbOUT.write(dataOUT)
        dbOUT.close()
        print()
        PrintX("***LICENSE KEY WORKED!***\n")
        time.sleep(0.8)
        main()
    elif(license==""):
        PrintZ("ENTERED NONE!\n")
        time.sleep(0.5)
        print()
        Print("See more from 'github.com/Pahasara'\n\n")
        time.sleep(4)
        Print("Thanks for choosing DvNET Parker...")
        print()
        time.sleep(5)
    else:
        PrintZ("INVALID LICENSE KEY!\n\n")
        time.sleep(0.5)
        EXactivate()      
    
#-- ACTIVATE --
def Activate():
    license = stdiomask.getpass(prompt=":> Enter license key to activate: ")
    if(license=="Dv43T-S41LK-H3L1O-W041D" or license=="Dv43T S41LK H3L1O W041D" or license=="Dv43TS41LKH3L1OW041D"):               
        dbOUT = open("Data/Database1.db", "r+")
        dataOUT = dbOUT.read()
        dbOUT.close()
        os.remove("Data/Database1.db")
        dataOUT = dataOUT.replace("*f#hj76go*","Dv43T-S41LK-H3L1O-W041D")
        dbOUT = open("Data/Database1.db", "w+")
        dbOUT.write(dataOUT)
        dbOUT.close()
        print()
        PrintX("***LICENSE KEY WORKED!***\n")
        time.sleep(0.8)
    elif(license==""):
        PrintZ("ENTERED NONE!\n")
        time.sleep(0.5)
    else:
        PrintZ("INVALID LICENSE KEY!\n\n")
        time.sleep(0.5)
        Activate()
# -----------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------
# ''' START UP --Parker.BOOT ''''
try:
    x = ""
    UserFile = open(Parker._userFile, "r")
    UserFile.close()
except IOError:
    time.sleep(1)
    print("<: Hi, you're welcome user.\n")
    time.sleep(1)
    print("<: ------------------------------------------------------")
    print("<:                   ***  SIGN UP  ***")
    print("<: ------------------------------------------------------")
    time.sleep(0.2)
    Username = input(":> " + "Enter your username here: ")
    Password = stdiomask.getpass(prompt=">: Enter your password here: ")
    os.mkdir("Data")
    win32api.SetFileAttributes('Data',win32con.FILE_ATTRIBUTE_HIDDEN)
    newRandFile = open("Data/RandomDB.db", "w+")
    #default values 4 RDB
    defaultRTX = "Hi, You're welcome to the Parker!;How are you?;_USER, you can use 'age' command to know Parker's age"
    newRandFile.write(defaultRTX)
    newRandFile.close()
    newDBFile0 = open("Data/Database0.db", "w+")
    #default values 4 DB0
    defaultDB0 = ";*f#hj86go*;*f#hj96go*;*f#hj76go*;*f#hl76go*;*f#hk76go*;*f#hd76go*;*f#hd75go*;hello;hi"
    newDBFile0.write(defaultDB0)
    newDBFile0.close()
    newDBFile1 = open("Data/Database1.db", "w+")
    #get datetime
    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day 
    dayz = 30
    #default values 4 DB1
    defaultDB1 = ";" + enc(Username) + ";" + enc(Password) +";*f#hj76go*;"+ enc(str(year)) + ";" + enc(str(month)) + ";" + enc(str(day)) +";"+ enc(str(dayz))+ ";Hello, how are you?;Hi, have a nice day _USER."
    newDBFile1.write(defaultDB1)
    newDBFile1.close()
    PrintX("SIGNUP SUCCESS\n")
    Print("------------------------------------------------------\n\n")
    time.sleep(0.8)
    Print("Hi, " + Username + ". You're welcome to Parker.\n\n")
    time.sleep(1)
    Print("HINT: Type 'help' or 'credits' for more information.\n")
    time.sleep(2)
    main()
else:
    Username = readUINFO()
    Password = readUINFO('pass')
    print("* Type 'help' or 'credits' for more information.")
    time.sleep(0.2)
    checkVALID()      
# -----------------------------------------------------------------------------------------------------


""" Scripted Date  : 2017.08.26 """
""" Script Updated : 2021.08.01 """

''' Ended Coding on 01/08/2021 '''