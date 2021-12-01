"""
Author: Gabriel Heinzer (dev@gabrielheinzer.ch)
__main__.py (c) 2021
Desc: This is a simple script for adding services in linux
Created:  2021-11-30T17:58:19.750Z
Modified: 2021-11-30T18:09:53.255Z
"""

def main():
    print("linux-add-service by Gabriel Heinzer\n")
    name = input("What should be the name of your service?: ")
    desc = input("Enter a short description about what your service will be doing: ")
    user = input("Which user should run the service (eg. root): ")
    wd = input("Please enter the working directory of your script: ")
    cmd = input("Please enter the path to the script that has to be executed: ")

if __name__ == "__main__":
    main()