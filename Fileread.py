# Automation script
# this script is used to read a file or data in file .
# if there is no file in this path. python script display message on screen there is no
# such file.


import os



def Readfile(FileName):
    if(os.path.exists(FileName)):
        fd = open(FileName,"r")
        Data = fd.read()
        print("Data from the file is")
        print(Data)
        fd.close
    else:
        print("There is no such file")
        return

def main():
    print("Enter a file name")
    Name = input()

    Readfile(Name)

if __name__ == "__main__":
    main()