# Overview
This is a very basic instant messaging application that can be used to communicate over text between two computers on a local area network. It is peer to peer where one user will 'host' the connection by running the host program and the other user will run the client program and input the host's local IP. After the connection is established, text messages can be sent back and forth between the machines until one or the other quit the program.

I wrote this program to learn the basics of socket programming and GUI creation in Python.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](https://youtu.be/pcFTHB9mjWk)

# Network Communication
This program utilizes a peer-to-peer architecture for a local area network.

The data transfer protocol used is TCP running on port 5580.

The messages that can be sent are text-only messages. 

# Development Environment
* Visual Studio Code
* Python 3.9.5 64bit
* Socket library
* tkinter library

# Useful Websites
* [Python Reference Library: Socket](https://docs.python.org/3.6/library/socket.html#other-functions)
* [Tk Tutorial](https://tkdocs.com/tutorial/index.html)
* [Python Socket Basics](https://www.tutorialspoint.com/python/python_networking.htm)


# Future Work
* Improve the send/receive loop to not slow down the process as much.
* Style and layout the Tk window to look more professional.
* Update the client program to have the host ip prompt and input be handled in the GUI.
* Clean up the quit conditions to not be so abrupt on the side who closed second.
