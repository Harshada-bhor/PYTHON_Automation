#Automation script which accept directory name from user and display all names &
#Duplicate files from that directory.and delete duplicated files and that deleted file
# store in log file which is created into current directory.
# and display execution time required for script..

import os
from sys import *
import hashlib
import time


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

def RemoveDuplicate(dict1,log_dir="Demo"):
    results = list(filter(lambda x:len(x)>1,dict1.values()))
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
        
    separator = "_" * 80
    log_path = os.path.join(log_dir, "log.txt.Log")
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Duplicate file process logger:" +time.ctime()+"\n")
    f.write(separator + "\n")

    if len(results)>0:
        f.write("Duplicate found.\n")
        f.write("The following files are identical and it would be deleted.\n")
        icnt=0;
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt >=2:
                    f.write('\t\t%s\n'%subresult)
                    os.remove(subresult)
    else:
        f.write("no Duplicate files found")

def main():
    print("___________python programming using automation__________")
    print("Application Name:" +argv[0])

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
        arr =findDuplicate(argv[1])
        RemoveDuplicate(arr)

    except ValueError:
        print("Error:Invalid Datatype of input")
    except Exception as E:
        print("Error:Invalid input",E)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
print("Execution time is :" ,end_time-start_time)


#input - python Executiontime_file.py Data    # data is the duplicate file folder