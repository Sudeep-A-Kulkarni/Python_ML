import psutil 
import os
import time

def CreateLog(FolderName):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    time_stamp = time.ctime()
    time_stamp = time_stamp.replace(" ","")
    time_stamp = time_stamp.replace(":","_")
    time_stamp = time_stamp.replace("/","_")
    
    FileName = os.path.join(FolderName, "Marvellous%s.log"%(time_stamp))

    fobj = open(FileName,"w")

    border = "_" * 80
    fobj.write(border+"\n")
    fobj.write("\t\tMarvellous Infosystems Process Log\n")
    fobj.write("\t\tLog file is created at : "+time.ctime()+"\n")
    fobj.write(border)

    


def ProcessScan():
    
    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            info["vms"] = proc.memory_info().vms / (1024 * 1024)
            listprocess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

def main():
    CreateLog("MarvellousProcess")


    


if __name__ == "__main__":
    main()