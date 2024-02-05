# This is Automation script.
# this script display foldername,subfolder and file in a given input folder.
# the input is a folder name which is present along with script file location.
# or input is a absolute or relative path which is given in dauble cotes.

from sys import *
import os


def DirectoryWatcher(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : " + foldername)
            for subf in subfolder:
                print("Sub folder of " + foldername + "is :" + subf)
            for filen in filname:
                print("File inside " + foldername + "is : " + filen)
            print(' ')
    else:
        print("Invalid Path")


def main():
    print("----- python Automation machine learning-----")

    print("Application name : " + argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()


#input - python DirectoryWatcher1.py Data   # the folder data is present same location of script file
#or - python DirectoryWatcher1.py "absolute path folder which is not present with script file location"