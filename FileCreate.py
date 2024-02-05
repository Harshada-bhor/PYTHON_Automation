# Automation script
# this script is used to create a new file if the file is already exists it gives
# message that "the file is already exists".


import os



def CreateFile(FileName):
    if(os.path.exists(FileName)):
        print("File is Already existing")
        return
    else:
        fd = open(FileName,"w")
        print("the new file has been created successfully.")


def main():
    print("Enter a file name to create")
    Name = input()

    CreateFile(Name)

if __name__ == "__main__":
    main()