# A Programme which accept file name from user and open that file and display the content
# of that file on screen.

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
    
