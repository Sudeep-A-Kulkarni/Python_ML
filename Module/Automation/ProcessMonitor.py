import psutil 
def ProcessDisplay():
    border = "*" * 25
    print(border)
    print("Information of currently running processes. ")
    print(border)

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid','name'])
        print(info)



def main():
    ProcessDisplay()



if __name__ == "__main__":
    main()