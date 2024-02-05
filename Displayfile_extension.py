#Automation script which accept directory name & file extention from user and
# display all files of that extention

import os
from sys import *
import hashlib


def DirectoryWatcher(path,extention):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : " + foldername)
            for filen in filname:
                path = os.path.join(foldername,filen)
                if filen.endswith(extention):
                    print("files found:", filen)

    else:
        print("Invalid Path")


def main():
    print("---- Directory automation using python -----")

    print("Application name : " + argv[0])

    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        DirectoryWatcher(argv[1],argv[2])


    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()

    # input- python Assignment10_1.py "path of directory" .py  or extension of file
