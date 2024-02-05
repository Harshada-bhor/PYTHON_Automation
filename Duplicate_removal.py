#Automation script which accept directory name from user and  remove
#Duplicate files from that directory.

import os
from sys import *
import hashlib
import time

def Deletefiles(dict1):
    results = list(filter(lambda x: len(x)>1,dict1.values()))

    icnt = 0;

    if len(results)>0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt >=2:
                    os.remove(subresult)
            icnt = 0
    else:
        print("no Duplicate files found")


def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf= afile.read(blocksize)
    
    while len(buf)>0:
        hasher.update(buf)
        buf= afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def findDuplicate(path):
    flag=os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)
       
    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirname, subdirs, Filelist in os.walk(path):
            print("Current folder name is : " + dirname)
        for filen in Filelist:
            path= os.path.join(dirname,filen)
            file_hash = hashfile(path)
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash]=[path]
        return dups
    else:
        print("Invalid path")

def PrintDuplicate(dict1):
    results = list(filter(lambda x:len(x)>1,dict1.values()))

    if len(results)>0:
        print("Duplicate found")
        print("The following files are identical.")
        icnt=0;
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt >=2:
                    print('\t\t%s'%subresult)
    else:
        print("no Duplicate files found")




def main():
    print("___________Python Automaion machine learning__________")
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
        arr={}
        starttime = time.time()
        arr =findDuplicate(argv[1])
        PrintDuplicate(arr)
        Deletefiles(arr)
        endtime = time.time()
    except ValueError:
        print("Error:Invalid Datatype of input")
    except Exception as E:
        print("Error:Invalid input",E)


if (__name__ == "__main__"):
    main()