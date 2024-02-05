# This is a Automation Template.
# input using commandline Arguments.
# this script use to chake the given number is even or odd.

from sys import *

def Script_Task(No):
    if(No%2==0):
        print("It is even number")
    else:
        print("It is Odd number")


def main():
    print("---------- Automations Using python ---------")
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

    else:
        Script_Task(int(argv[1]))


if __name__=="__main__":
    main()



    # input - python AutomationTemplate.py 8