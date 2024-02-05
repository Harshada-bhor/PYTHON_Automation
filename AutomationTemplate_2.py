# This is a Automation Template
# input using commandline Arguments.


from sys import *

 
def fun(parameter):
   #logic of script


def main():
    print("----------- Automations Using python ---------")
    print("Application name:",+argv[0])

    if(len(argv) !=3):
        print("Error: Insufficint arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if((argv[1] == "-h" )or (argv[1]=="-H")):
        print("Help:This script used to perform__")
        exit()

    if((argv[1] == "-u") or (argv[1]== "-U")):
        print("Usage: provide _____number of arguments as"Application_Name____ or "")
        print( "First arguments as:----------")
        print(" second arguments as:___________")
        exit()

    try:
        fun(argv[1])

    except Exception as E:
        print("Error : Invalid input" + E)

    if ((len(argv)<1) or (len(argv)>3)):
        print("Error: Invalid number of arguments")

if __name__=="__main__":
    main()

    # input - python filename.py inputnumber