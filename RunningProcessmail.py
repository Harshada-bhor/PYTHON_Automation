#Automation script which accept directory name from user and create log file in that
# directory which contains information of all running processes.
# and this file to specific mail.

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


def MailSender(filename,time):
    try:
        fromaddr = "-------------@gmail.com"
        toaddr = "---------@gmail.com"

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
         """%(toaddr,time)

        Subject = """
        
        Python Automation & ml learning Process log generated at :%s
        
        """%(time)

        msg["Subject"] = Subject

        msg.attach(MIMEText(body,"plain"))

        attachment = open(filename,"rb")

        p = MIMEBase("application","octet-stream")

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header("Content-Disposition","attachment;filename=%s" %filename)

        msg.attach(p)

        s= smtplib.SMTP("smtp.gmail.com",587)

        s.starttls()

        s.login(fromaddr, "-------------")

        text = msg.as_string()

        s.sendmail(fromaddr,toaddr,text)

        s.quit()

        print("Log file successfully sent through Mail")

    except Exception as E:
        print("Unable to send mail.",E)

def ProcessLog(log_dir="Marvellous"):
    listprocess = []
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
        
    separator = "_" * 80
    log_path = os.path.join(log_dir, "MarvellousLog%s.log"%(time.time()))
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Python Automation & Ml learning process logger:"+time.ctime() +"\n")
    f.write(separator + "\n")
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            listprocess.append(pinfo);
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n"%element)

    print("Log file is successfully generated at location %s"%(log_path))

    connected = is_connected()

    if connected:
        startTime = time.time()
        MailSender(log_path,time.ctime())
        endTime = time.time()
        print("Took %s seconds to send mail" %(endTime-startTime))
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
        print("Usage : Application_name Directory_Name")
        exit()




    try:
        ProcessLog(argv[1])
        
    except ValueError:
        print("Error:Invalid Datatype of input")
    except Exception as E:
        print("Error:Invalid input",E)


if (__name__ == "__main__"):
    main()


    #input - python RunningProcessmail.py Data