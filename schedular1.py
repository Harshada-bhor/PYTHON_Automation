# This is using Automation .
# use for repeated task.
# schedule the task to perform.

import schedule
import time
import datetime

def Fun():
    print("Inside Fun")

def main():
    print("Inside task scheduler")


    schedule.every(1).minutes.do(Fun)   # the function Fun() run in every 1 minutes.

    while(True):
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()
    
    
