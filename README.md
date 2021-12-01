<!--
Author: Gabriel Heinzer (dev@gabrielheinzer.ch)
README.md (c) 2021
Desc: README.md for gheinzer/py_scripts
Created:  2021-12-01T18:50:09.813Z
Modified: 2021-12-01T19:02:31.094Z
-->

# py_scripts

This repository is supposed to contain some useful scripts. These scripts are described here. I DO NOT GUARANTEE THAT ANY OF THESE SCRIPTS WORK. However, if you have a problem with it, post an issue or, even better, fix it and send a pull request.

## `linux-add-service.py`

This script can help you when you want to add a service to a Linux machine.
You can use the following command line arguments:

```
-f  Force the execution and ignore detected OS.
-h  Display a help
```

It will then ask you a few questions about your service:

```
What should the name of your service be?: foo
Enter a short description about what your service will be doing: bar
Which user should run the service (eg. root): foobar
Please enter the working directory of your script: /foo/bar/
Please enter the path to the script that has to be executed: /foo/bar/something.sh
Do you want to restart the service after it stops? (no, always, on-failure, on-abnormal, on-watchdog, on-success): always
```

After that, it will create the service file (in `/etc/systemd/system/`) and
run `systemctl deamon-reload`. **For these both operations to work, you should execute this script as root.**

If you need help with the `.service` files or the question about the restart mode, you can find a good help here: https://www.freedesktop.org/software/systemd/man/systemd.service.html.
