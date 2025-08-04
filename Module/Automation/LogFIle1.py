import sys
import time

def main():
    time_stamp = time.ctime()
    #print(time_stamp)
    fobj = open("MarvellousLog.log","w")

    Border = "-"*54

    fobj.write(Border + "\n")
    fobj.write("this is a log file of marvellous sutomation script \n")
    #fobj.write(time_stamp + "\n")
    fobj.write(Border+ "\n")
    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    fobj.write(Border+ "\n")
    fobj.write("this was created at " + time_stamp + "\n")
    fobj.write(Border+ "\n")

if __name__ == "__main__":
    main()