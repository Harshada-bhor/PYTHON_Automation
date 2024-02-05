## Automation script
# this script is used to write data in file .
# if there is no file in this path. python script display message on screen there is no
# such file.



import os


def Writefile(FileName):
    if(os.path.exists(FileName)):
        print("Enter a Data that you want write in file")

        Data = input()
        fd = open(FileName, "a")
        fd.write(Data)
        fd.close
    else:
        print("There is no such file")
        return

def main():
    print("Enter a file name")
    Name = input()

    Writefile(Name)

if __name__ == "__main__":
    main()