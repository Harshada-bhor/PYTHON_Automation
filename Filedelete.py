# Automation script
# this script is used to delete a file.
# if there is no file in this path. python script display message on screen there is no
# such file.





import os



def Deletefile(FileName):
    if(os.path.exists(FileName)):
        os.remove(FileName)
    else:
        print("There is no such file")

def main():
    print("Enter a file name ")
    Name = input()

    Deletefile(Name)

if __name__ == "__main__":
    main()