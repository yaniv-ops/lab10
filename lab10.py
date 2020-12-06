def menu():
    while(True):
        CHOICE=input("Enter your choice:\n1.Show Ip Details\n2.show your DNS details\n")
        if (CHOICE == "1"):
            IP_SHOW()
        elif (CHOICE == "2"):
            print(CHOICE)
        else:
            print("Chosse 1 or 2 only!!!")



def IP_SHOW():
    while(True):
        IP_CHOICE=input("1.Add Ip address\n2.Remove Ip address\n3.print all Ip's\n")
        if (IP_CHOICE == "1"):
            IP = input("Enter an IP:\n")
            if (IP in IP_LIST):
                print("Ip is in The list:\n" + str(IP_LIST) + "\n")
            else:
                IP_LIST.append(IP)
                print("Ip is added to the list:\n" + str(IP_LIST) + "-------------------\n")
            YES_NO=input("Would you like to continue? y/n")
            if (YES_NO == "y"):
                continue
            else:
                break
        elif (IP_CHOICE == "2"):
            DEL_IP=input("Enter Ip to delete:")
            if (DEL_IP in IP_LIST):
                IP_LIST.remove(DEL_IP)
            print("you're list updated:\n" + str(IP_LIST) + "--------------\n")
        else:
            print("Ip is not in list" + str(IP_LIST) + "-------------\n")
        YES_NO = input("Would you like to continue? y/n")
        if (YES_NO == "y"):
            continue
        else:
            break
def DNS_SHOW():
    MY_DICT={}
    while(True):
        DNS=input("Enter a web DNS:\n")
        ADD=input("Enter Ip adrsress of site:\n")
        MY_DICT["DNS"]=[ADD]
        print(MY_DICT)







IP_LIST=[]
menu()
