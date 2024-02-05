#Automation script which accept Two directory name and one extension from user and copy all files
# from first to secondary directory with specified extension.

import os
from sys import *
import shutil


def DirectoryWatcher(path1,path2,extention):
    if not os.path.exists(path2):
        try:
            os.mkdir(path2)
        except:
            pass

    flag = os.path.isabs(path1)
    if flag == False:
        path1 = os.path.abspath(path1)

    exists = os.path.isdir(path1)

    if exists:
        for foldername, subfolder, filname in os.walk(path1):
            print("Current folder is : " + foldername)
            for filen in filname:
                path1 = os.path.join(foldername,filen)
                if filen.endswith(extention):
                    shutil.copy(path1, path2)
                    print("copied", filen)

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
