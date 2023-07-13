# AirBnB Clone Project - The Console

![AirBnB Logo](https://github.com/habeebdindi/AirBnB_clone/blob/master/AirBnB_Logo/Logo.png)


## Description Of Project
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this project, we build the AirBnB clone console. This is the first important step towards building our first full stack web application: the <strong>AirBnB clone.</strong>. We are building a command interpreter using Python.


## Description Of The Command Interpreter
<strong>The command interpreter</strong> is exactly a shell but it is <em>limited to a specific user-case</em>. It accepts <strong>limited commands</strong>, and these commands have been <strong><em>defined solely for the purpose of the usage of the AirBnB website</em></strong>.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The commands accepted by the CMD are In this case, we are using the AirBn console to:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc.
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This basically helps us to manage the backend and file storage system.


### How To Start The CMD
#### Steps to install and use the command line interpreter
----------------------------------------------------------
1. Clone the repository into your local machine: ``git clone https://github.com/habeebdindi/AirBnB_clone.git``
2. Navigate to the cloned repo: ``cd AirBnB_clone``
3. In your local repo, you will see alot of files. There is a file named <strong><em>console.py</em></strong>. The command interpreter is launched by running the <strong><em>console.py</em></strong>:    ``./console.py``

The commands accepted by the interpreter are:
- EOF
- help
- quit


### How To Use The CMD
The CMD works in two different modes: The <strong>Interactive Mode</strong> and the <strong>Non-interactive Mode.</strong>


#### Interactive Mode
In **Interactive mode**, the console will display a prompt <strong>(hbnb)</strong> indicating that <em>the user can write and execute a command</em>. After the command is run, the prompt will appear again a wait for a new command. This will <em>go on indefinitely as long as the user does not exit the program</em>.

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```


#### Non-interactive Mode
In **Non-interactive mode**, <strong>the shell will need to be run with a command input piped into its execution</strong> so that the command is run as soon as the Shell starts. In this mode, no prompt will appear, and no further input will be expected from the user.

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):========================================
EOF  help  quit
(hbnb)
$
```
