import os, time, platform

#



n = ["no", "n"]
y = ["yes", "y"]

#-----------------------------------------------------------------------------------------------
def program():
    os.system("clear")
    min = input("Minimum size of pass length ")
    max = input("Maximum size of pass length ")
    name = input("Name of file ")
    os.system("clear")
    print("Please copy the BSSID that will be printed out below")
    print()
    time.sleep(4)
    os.system("aircrack-ng "+name+".cap") 
    list = []
    e = ",()'"
    print()
    b = input("Please specify the BSSID ") 
    os.system("clear")
    print("Choose one of the following:")
    print("l - lowercase")
    print("c - capitals")
    print("n - numbers")
    print("lc - capitals and lowercase")
    print("ln - lowercase and numbers")
    print("cn - capitals and numbers")
    print("a - capitals, lowercase and numbers")
    c = input("").lower()
    os.system("clear")
            
#----------------------------------------------------------------------------------------------------------            
    if c == "l":
        la = "abcdefghijklmnopqrstuvwxyz"
        command = "crunch ",min," ",max, " ",la," | aircrack-ng --bssid ",b," -w- ",name,".cap"
        for l in command:
            if l not in e:
                list.append(l)
        
        os.system((str(''.join(list))))
#----------------------------------------------------------------------------------------------------------                     
    if c == "c":
        ca = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        command = "crunch ",min," ",max, " ",ca," | aircrack-ng --bssid ",b," -w- ",name,".cap"
        for l in command:
            if l not in e:
                list.append(l)
        os.system((str(''.join(list))))
#----------------------------------------------------------------------------------------------------------            
    if c == "n":
        na = "0123456789"
        command = "crunch ",min," ",max, " ",na," | aircrack-ng --bssid ",b," -w- ",name,".cap"
        for l in command:
            if l not in e:
                list.append(l)
        os.system((str(''.join(list))))
#----------------------------------------------------------------------------------------------------------                     
    if c == "lc":
        lca = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        command = "crunch ",min," ",max, " ",lca," | aircrack-ng --bssid ",b," -w- ",name,".cap"
        for l in command:
            if l not in e:
                list.append(l)
        os.system((str(''.join(list))))
#-----------------------------------------------------------------------------------------------------------                
    if c == "ln":
        lna = "abcdefghijklmnopqrstuvwxyz0123456789"
        command = "crunch ",min," ",max, " ",lna," | aircrack-ng --bssid ",b," -w- ",name,".cap"
        for l in command:
            if l not in e:
                list.append(l)
        os.system((str(''.join(list))))
#-------------------------------------------------------------------------------------------------------------                            
    if c == "cn":
        cna = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        command = "crunch ",min," ",max, " ",cna," | aircrack-ng --bssid ",b," -w- ",name,".cap"
        for l in command:
            if l not in e:
                list.append(l)
        os.system((str(''.join(list))))
#-------------------------------------------------------------------------------------------------------------                
    if c == "a":
        aa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        command = "crunch ",min," ",max, " ",aa," | aircrack-ng --bssid ",b," -w- ",name,".cap"
        for l in command:
            if l not in e:
                list.append(l)
        os.system((str(''.join(list))))  
#-----------------------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
def linux(c):
    if c in y:
        print("Sit back it may take a while...")
        time.sleep(4)
        os.system("clear")
        print("Updating System...")
        time.sleep(1)
        os.system("sudo apt-get update")
        os.system("clear")
        print("Upgrading System...")
        time.sleep(1)
        os.system("sudo apt-get upgrade")
        os.system("clear")
        print("Dis-Upgrade...")
        time.sleep(1)
        os.system("sudo apt-get dist-upgrade")
        os.system("clear")
        print("Installing aircrack-ng...")
        time.sleep(1)
        os.system("sudo apt-get install aircrack-ng")
        os.system("clear")
        print("Installing crunch...")
        os.system("sudo apt-get install crunch")
        os.system("clear")
        time.sleep(1)
        program()
    else:
        program()
#-------------------------------------------------------------------------------------            
        
        
def rest():
    #TODO add "support" for windows
    print("Sorry This Program Is Not Built For Your OS")
    input("Press enter to exit... ")



os1 = platform.system()
if os1 == "Linux":
    os.system("clear")
    choice = input("Do you want to install aircrack and crunch ").lower()
    while choice not in n and choice not in y:
        choice = input("Please input yes or no ").lower()
    linux(choice)
elif os1 == "Windows":
    os.system("cls")
    rest()
else:
    rest()