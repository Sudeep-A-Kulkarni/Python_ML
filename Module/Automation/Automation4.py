import schedule 
import time 
import datetime

def MySchedule():
    print("inside MySchedule function at : ",datetime.datetime.now())

def main():
    print("Inside automation script.")
    print("current time is : ",datetime.datetime.now())

    schedule.every(20).seconds.do(MySchedule)

    print("Application is in wating state : ")
    
    while(True):
        schedule.run_pending()
        time.sleep(1)
        
        



if __name__ == "__main__":
    main()