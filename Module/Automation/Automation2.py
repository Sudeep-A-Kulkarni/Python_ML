import schedule
import time 
import datetime

def MySchedule():
    print("inside MySchedule function at : ",datetime.datetime.now())

def main():
    print("Inside automation script.")
    print("current time is : ",datetime.datetime.now())

    schedule.every(20).seconds.do(MySchedule)

    print("end of automation script")



if __name__ == "__main__":
    main()