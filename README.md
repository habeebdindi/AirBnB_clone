# AIRBNB CLONE
Built using python language

# DESCRIPTION

This project implements the Airbnb clone It uses the BaseModel class as the super class the datetime, cmd and uuid modules are used in its implementation The command interpreter works in interactive and non-interactive mode. Every directory is a package.

# COMMAND INTERPRETER
First you have to clone this entire repository into your local terminal to run the commands.
How to start it:

The command interpreter(shell) is started by running the console.py module:

sasaka-jr@Sasaka-JR:~/AirBnB_clone$ ./console.py

Usage

It(coommand interpreter) supports various commands: -create -destroy -all -update -quit

# create

Creates new instance of BaseModel and saves it to the JSON file and prints a unique id:

sasaka-jr@Sasaka-JR:~/AirBnB_clone$ create BaseModel

# destroy

Deletes an instance based on the class name and id(changes are saved in the JSON file):

sasaka-jr@Sasaka-JR:~/AirBnB_clone$ destroy BaseModel 1243-1243-1243

# all

Prints string representation of all instances:

sasaka-jr@Sasaka-JR:~/AirBnB_clone$ all

Also prints the string representation of a specified instance:

sasaka-jr@Sasaka-JR:~/AirBnB_clone$ all BaseModel 1243-1243-1243

# update

Updates instances based on the class name and id by adding or updating an attribute(saved to the JSON file):

sasaka-jr@Sasaka-JR:~/AirBnB_clone$ update BaseModel 1243-1243-1243 email "sasakajr@gmail.com"

# quit

Quits the console:

sasaka-jr@Sasaka-JR:~/AirBnB_clone$ quit

Thank you for using the HBNB console.



# FRONT END

An interactive graphical user interface
