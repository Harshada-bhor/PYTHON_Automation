#Automation script which accept directory name from user and display all names &
#Duplicate files from that directory.and delete duplicated files and that deleted file
# store in log file which is created into current directory.and this file send to specific
# mail.

import os
import psutil
import urllib.request
import smtplib
from sys import *
import hashlib
import time
import schedule
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    cmd = os.system('ping google.com -w 4 > clear')
    if cmd == 0:
        return True
    else:
        return False


def MailSender(filename, time):
    try:
        fromaddr = "bhorharshada884@gmail.com"
        toaddr = "hbhor042@gmail.com"

        msg = MIMEMultipart()

        msg["From"] = fromaddr

        msg["To"] = toaddr

        body = """
        Hello %s,
        Welcome to Marvellous Infosystem.
        please find attached document which contains Log of running process.
        Log file is created at: %s

        This is auto generated mail.

        Thanks & regards,
        harshada shankar Bhor
         """ % (toaddr, time)

        Subject = """

        Python Automation & ml learning Process log generated at :%s

        """ % (time)

        msg["Subject"] = Subject

        msg.attach(MIMEText(body, "plain"))

        attachment = open(filename, "rb")

        p = MIMEBase("application", "octet-stream")

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header("Content-Disposition", "attachment;filename=%s" % filename)

        msg.attach(p)

        s = smtplib.SMTP("smtp.gmail.com", 587)

        s.starttls()

        s.login(fromaddr, "cznzefcnpgwnggph")

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)

        s.quit()

        print("Log file successfully sent through Mail")

    except Exception as E:
        print("Unable to send mail.", E)

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


        connected = is_connected()

        if connected:
            startTime = time.time()
            MailSender(log_path, time.ctime())
            endTime = time.time()
            print("Took %s seconds to send mail" % (endTime - startTime))
        else:
            print("There is no internet connection")


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


if (__name__ == "__main__"):
    main()


#input - python duplicateremovalfile_mail.py Data     #( data is the duplicate file folder)
