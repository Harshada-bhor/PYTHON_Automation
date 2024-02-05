# A Programme which accept file name from user and create a new file name "Demo.txt."
# copy all content from existing file into new file .


import os
from sys import*

def Copyfile(second_file):

    fd1= open('Demo.txt','w')
    fd2= open(second_file,'r')
    for line in fd2:
        fd1.write(line)


def main():
    print("----Application of create and copy file -----")

    if (len(argv) < 2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    Copyfile(argv[1])



if __name__ == "__main__":
    main()