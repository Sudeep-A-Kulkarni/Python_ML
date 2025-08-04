import schedule 
import time 
import datetime

def MySchedule():
    print("inside MySchedule function at : ",datetime.datetime.now())

def MyScheduleX():
    print("inside my scheduleX function at : ",datetime.datime.now())

def main():
    print("Inside automation script.")
    print("current time is : ",datetime.datetime.now())

    schedule.every(20).seconds.do(MySchedule)
    schedule.every(1).minute.do(MyScheduleX)
    schedule.every(1).hour.do(MyScheduleX)



    print("Application is in wating state : ")
    while(True):
        schedule.run_pending()
        time.sleep(1)
        
        



if __name__ == "__main__":
    main()