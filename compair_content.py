# A Programme which accepttwo file name for users and compair content of both files
# if both files content same display success and if content is not same display failure


import os
from sys import*



def Compairfile(first_file,second_file):

    fd1= open(first_file,'r')
    fd2= open(second_file,'r')
    i=0
    for Data1 in fd1 :
        i+=1

    for Data2 in fd2 :

        if Data1 == Data2:
            print("Display Success")
        else:
            print("Display failure")
            break
    fd1.close()
    fd2.close()


def main():
    print("----Application of compair content of file -----")

    if (len(argv) < 3):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()


    Compairfile(argv[1],argv[2])





if __name__ == "__main__":
    main()