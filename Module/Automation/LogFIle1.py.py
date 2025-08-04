import sys

def main():
    border = "-"*69
    print(border)
    print("-------------------Marvellous Automations----------------------------")
    print(border)

    # Logic
    if (len(sys.argv) == 2):
        if ((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
            print("this application is used to perform ----")
            print("this is the automation script")

        elif (((sys.argv[1])=="--U") or (sys.argv[1]=="--u")):
            print("Use the given script as .")
            print("ScriptName.py Arguement1 Arguement2")

        else:
            print("use the given flags as : ")
            print("--h : used to display the help.")
            print("--u : used to display the usage.")


    else:
        print("invalid number of command line arguements. ")
        print("use the given flags as : ")
        print("--h : used to display the help.")
        print("--u : used to display the usage.")
        
    print(border)
    print("----------------Thank you for using our script-----------------------")
    print("-------------------Marvellous Infosystems----------------------------")
    print(border)

if __name__ == "__main__":
    main()