#Automation script which accept directory name and two file extention from user and rename all 
# files with first extention to second extention.

import os
from sys import *
import hashlib


def DirectoryWatcher(path,extention1,extention2):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : " + foldername)
            for filen in filname:
                path = os.path.join(foldername,filen)
                if filen.endswith(extention1):
                    print("files found:", filen)
                    os.rename(filen,extention2)

    else:
        print("Invalid Path")


def main():
    print("---- Directory automation using python-----")

    print("Application name : " + argv[0])

    if (len(argv) != 4):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        DirectoryWatcher(argv[1],argv[2],argv[3])


    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
