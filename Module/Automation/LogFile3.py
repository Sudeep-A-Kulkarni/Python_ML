import sys
import time
def Create_Log():
    time_stamp = time.ctime()

    filename = "MarvellousLog%s.log" %(time_stamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")
    
    fobj = open(filename,"w")

    Border = "-"*54

    fobj.write(Border + "\n")
    fobj.write("this is a log file of marvellous sutomation script \n")
  
    fobj.write(Border+ "\n")
    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    fobj.write(Border+ "\n")
    fobj.write("this was created at " + time_stamp + "\n")
    fobj.write(Border+ "\n")

def main():
    Create_Log()

    


if __name__ == "__main__":
    main()