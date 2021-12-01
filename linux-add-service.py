"""
Author: Gabriel Heinzer (dev@gabrielheinzer.ch)
__main__.py (c) 2021
Desc: This is a simple script for adding services in linux
Created:  2021-11-30T17:58:19.750Z
Modified: 2021-12-01T19:04:31.271Z
"""
import os
import sys
import platform
def main():
    if("-h" in sys.argv):
        print("""
        
        linux-add-service by Gabriel Heinzer
        These are the arguments you can pass:
            -f  Force the execution and ignore detected OS.
            -h  Display this help
        """)
    if(platform.system() != "Linux" and not "-f" in sys.argv):
        print("You do not seem to run Linux. If you execute this on linux, but this error message appears, try running this script with -f.")
        exit()
    inputValid = False
    while not inputValid:
        print("linux-add-service by Gabriel Heinzer\n")
        name = input("What should the name of your service be?: ")
        desc = input("Enter a short description about what your service will be doing: ")
        user = input("Which user should run the service (eg. root): ")
        wd = input("Please enter the working directory of your script: ")
        cmd = input("Please enter the path to the script that has to be executed: ")
        restartmode = input("Do you want to restart the service after it stops? (no, always, on-failure, on-abnormal, on-watchdog, on-success): ")

        if(not restartmode in ["no", "always", "on-failure", "on-abnormal", "on-watchdog", "on-success"]):
            print("Your input for the restart mode is not valid. Please try again.")
            continue

        if(not "" in (name, desc, user, wd, cmd, restartmode)):
            inputValid = True
        else:
            print("Invalid input. Please try again.")
            continue

        if(not os.path.exists(wd) or not os.path.exists(cmd)):
            inputValid = False
            print("The working directory or the script path are incorrect (files do not seem to exist). Please try again.")
            continue
    
    serviceFileContent = f"""
    [Unit]
    Description={desc}

    [Service]
    User={user}
    WorkingDirectory={wd}
    ExecStart={cmd}
    Restart={restartmode}

    [Install]
    WantedBy=multi-user.target
    """
    filepath = f"/etc/systemd/system/{name}.service"

    if(os.path.exists(filepath)):
        if(not input("A service with this name already exists. Do you want to overwrite it? (y, N): ").upper() == "Y"):
            exit()
            

    sys.stdout.write("\nInstalling service... : Creating service file...")

    try:
        serviceFile = open(filepath, "w")
        serviceFile.write(serviceFileContent)
        serviceFile.close()
    except PermissionError:
        print("Was not able to create the file due to a permission error. Please rerun this script as root.")

    sys.stdout.write("\rInstalling service... : Running deamon-reload...    ")

    os.system("systemctl daemon-reload")


if __name__ == "__main__":
    main()