# This is using Automation .
# use for repeated task.
# schedule the task to perform.


import schedule
import time
import datetime
from sys import*

as_counter=0
def Task_Minutes():
    print("Task based on minutes get schedule at:",datetime.datetime.now())
    if as_counter==2:
        sys.exit()

def Task_Hour():
    print("Task based on hour get schedule at:",datetime.datetime.now())

def Task_Day():
    print("Task based on day get schedule at:",datetime.datetime.now())

def Task_Afternoon():
    print("Task based on day get schedule at:",datetime.datetime.now())


def main():
    print("Inside task scheduler")
    print("Current time is:",datetime.datetime.now())

    schedule.every(1).minutes.do(Task_Minutes)
    schedule.every(1).hour.do(Task_Hour)
    schedule.every(1).saturday.at("18:00").do(Task_Day)
    schedule.every(1).sunday.do(Task_Day)
    schedule.every(1).day.at("00:00").do(Task_Afternoon)

    while(True):
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()
    
    
