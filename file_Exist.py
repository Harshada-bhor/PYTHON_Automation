# Programme which accepts file name from user and chake whether that the exists current
# directory or not.
# in file name give extension properly.



import os



def Chkfile(FileName):
    if(os.path.exists(FileName)):
        print("File is existing")
    else:
        print("File is Not existing")
def main():
    print("Enter a file ")
    Name = input()

    Chkfile(Name)

if __name__ == "__main__":
    main()


    
    
