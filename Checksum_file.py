#Automation script which accept directory name from user and display all names &
#checksum of file from that directory

import os
from sys import *
import hashlib


def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf= afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf= afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def DisplayChecksum(path):
    flag=os.path.isabs(path)
    if flag == False:
       path = os.path.abspath(path)
    exists = os.path.isdir(path)

    if exists:
        for dirname, subdirs, Filelist in os.walk(path):
            print("Current folder name is : " + dirname)
        for filen in Filelist:
            path= os.path.join(dirname,filen)
            file_hash = hashfile(path)
            print(path)
            print(file_hash)
            print(" ")
    else:
        print("Invalid path")


def main():
    print("___________Python Automaion machine learning __________")
    print("Application Name:"+argv[0])

    if (len(argv) != 2):
        print("Insufficient arguments")
        exit()

    if (argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if (argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name")
        exit()

    try:
        arr= DisplayChecksum(argv[1])
    except ValueError:
        print("Error:Invalid Datatype of input")
    except Exception as E:
        print("Error:Invalid input",E)


if (__name__ == "__main__"):
    main()

    # input - python Checksum.py Data   # the folder data is present same location of script file
    # or - python Checksum3.py "absolute path folder which is not present with script file location"