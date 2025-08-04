import psutil 
def ProcessDisplay():
    border = "*" * 25
    print(border)
    print("Information of currently running processes. ")
    print(border)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            info["vms"] = proc.memory_info().vms / (1024 * 1024)
            print(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass



def main():
    ProcessDisplay()



if __name__ == "__main__":
    main()