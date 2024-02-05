# Automation script which display specific running processes.

import psutil
import os
from sys import*
import time

def checkIfProcessRunning(processName):

    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
            return false

def findProcessIdByName(processName):
    
    listOfProcessObjects = []
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    for elem in listOfProcessObjects:
        print("Process Exists:\n" +"PID and other details are:\n",elem)

def main():
    print("------------python automation and machine learning---------")
    print("Automation script started with name:", argv[0])

    if (len(argv) != 2):
        print("Error: Insufficint arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if ((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help:This script used to perform__")

    elif ((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage: provide _____number of arguments as")
        print("First arguments as:----------")
        print(" second arguments as:___________")
        exit()

    try:
        Yes=checkIfProcessRunning(argv[1])

        if Yes:
            findProcessIdByName(argv[1])
        else:
            print('No such process Exists')


    except ValueError:
        print("Error:Invalid Datatype of input")
    except Exception:
        print("Error: Invalid Input")

if __name__=="__main__":
    main()

    # input - python Inforunning_process.py Notepad