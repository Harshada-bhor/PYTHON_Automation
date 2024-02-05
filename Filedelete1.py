# Automation script
# this script is used to delete a file.
# if the file is empty it directly deleted.
# if the file is not empty it ask to delete the file surely . if we say yes it delete
# permnently, and if we say no it will be not delete.
# if there is no file in this path. python script display message on screen there is no
# such file.


import os



def Deletefile(FileName):
    if(os.path.exists(FileName)):
        size = os.path.getsize(FileName)
        if(size==0):
            os.remove(FileName)
        else:
            print("Are u sure to delete the file? Y/N")
            option = input()
            if(option == "Y" or option == "y"):
                os.remove(FileName)
            else:
                print("File deletion process is stoped")

    else:
        print("There is no such file")

def main():
    print("Enter a file name")
    Name = input()

    Deletefile(Name)

if __name__ == "__main__":
    main()