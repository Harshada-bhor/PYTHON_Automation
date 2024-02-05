# Demonstration of commandline argument.
# this script is for addition of two numbers and # input numbers using commandline argument.


import sys

print("-------------Automation using python ------------")
print("Demonstration of Command Line Arguments ")
print("Application name:"+ sys.argv[0])

x = int(sys.argv[1])
y = int(sys.argv[2])
z = x+y

print(z)


# input - python CommandLineArgument.py  5 8