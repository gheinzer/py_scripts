"""
Author: Gabriel Heinzer (dev@gabrielheinzer.ch)
linux-add-command-alias.py (c) 2021
Desc: This script helps adding command aliases in linux.
Created:  2021-12-01T19:33:33.153Z
Modified: 2021-12-01T19:45:32.055Z
"""
import os
import sys
import platform
def main():
    print("linux-add-command-alias by Gabriel Heinzer")
    if("-h" in sys.argv):
        print("""
linux-add-command-alias by Gabriel Heinzer
These are the arguments you can pass:
    -f  Force the execution and ignore detected OS.
    -h  Display this help
        """)
        exit()
    if(platform.system() != "Linux" and not "-f" in sys.argv):
        print("You do not seem to run Linux. If you execute this on linux, but this error message appears, try running this script with -f.")
        exit()
    if(not os.path.exists("~/.bashrc")):
        print("~/.bashrc file does not exist.")
        exit()

    inputValid = False
    while not inputValid:
        name = input("What should the name of the alias, the short command, be?: ")
        cmd = input("For which command should it be an alias (which command should be executed when the alias name is executed)?: ")

        if("" in (name, cmd)):
            inputValid = False
            print("Your input is invalid. Please try again.")
            continue
        else:
            inputValid = True

    print("Writing file...")
    bashrc = open("~/.bashrc", "a")
    bashrc.write(f'\nalias {name}="{cmd}"')
    print("Finished.")

if __name__ == "__main__":
    main()