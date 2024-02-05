#Automation script which accept directory name from user and create log file in that
# directory which contains information of all running processes.

import os
import psutil
import time
from sys import *

 
def ProcessDisplay(log_dir = "Data"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    log_path= os.path.join(log_dir,"MarvellousLog%s.log"%(time.time()))
    f = open(log_path,'w')
    f.write(separator + "\n")
    f.write(" Process Logger:"+time.ctime()+"\n")
    f.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms']= vms
            listprocess.append(pinfo);
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

def main():
    print("------------ Automations using python ---------")
    print("Automation script started with name:",argv[0])

    if(len(argv) !=2):
        print("Error: Insufficint arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if((argv[1] == "-h" )or (argv[1]=="-H")):
        print("Help:This script used to perform__")

    elif((argv[1] == "-u") or (argv[1]== "-U")):
        print("Usage: provide _____number of arguments as")
        print( "First arguments as:----------")
        print(" second arguments as:___________")
        exit()

    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error:Invalid Datatype of input")
    except Exception:
        print("Error: Invalid Input")

if __name__=="__main__":
    main()


    #input= python Log_file.py Data