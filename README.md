# # Overview

With this project, I wanted to learn how networking works. What I expected to accomplish from this project was being able to understand how to use sockets to communicate from a server to a client and vice versa. I also wanted to learn how two clients can message each other which required the server to handle their messages.

The network program that I wrote is all in Python. I have two files which is the client and server. Start by running the server. Once the server is running move on to the client file and run it. It will ask for a nickname which will be the username that will identify that client. 

I wrote this application because I wanted to have a better understanding how networking works, and I wanted to create a group chat messenger. 

# Network Communication

The server will receive and handle any incoming clients that are trying to send a message. The client will send and receive information that the server will send back.

I am using TCP and the port number is 5050

The kind of format that is being used is ascii.

# Development Environment

I used the socket library and threading library in Python. The socket is used to connect the client and server to an IP address and a port.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Socket Programming in Python](https://realpython.com/python-sockets/)
* [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)

# Future Work

* Provide a GUI for the user
* Allow any client over the internet be able to connect to the server with permission.