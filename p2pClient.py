# Import needed libraries
import socket
from tkinter import *
from tkinter import ttk

# Open Client socket 
s = socket.socket()
name = socket.gethostname()
port = 5580

# Create the window
root = Tk()
root.title("P2P Client")
root.geometry("300x300")

# Put a grid frame inside to manage everything
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

# mysend method sends until the buffer is empty
def mysend(*args):
    # Extract message from input box and encode as binary for
    # sending
    msg = text.get().encode()
    # Quit condition
    if msg.decode() == 'quit':
        s.close()
        root.destroy()
    # Take length so we know how much to send
    MSGLEN = len(msg)
    totalsent = 0
    # Start sending
    while totalsent < MSGLEN:
        sent = s.send(msg[totalsent:])
        # If message is done, stop sending
        if sent == 0:
            break
        # Update total
        totalsent = totalsent + sent
    # Clear the input box
    text.set("")

# myreceive is an idle receive that takes in any incoming data,
# decodes it to a string, and updates the screen to show it.
def myreceive(self):
    try:
        global receive
        receive.set(s.recv(1024).decode())
    except socket.timeout:
        pass
    self.after(500, myreceive, self)



# Text entry box creation
text = StringVar()
text_entry = ttk.Entry(mainframe, width=20, textvariable=text)
text_entry.grid(column=0, row=1, sticky=(W, S))

# Incoming text message 
receive = StringVar()
ttk.Label(mainframe, textvariable=receive, wraplength=200).grid(column=0, row=0, sticky=(W, E))

# Send button 
ttk.Button(mainframe, text="Send", command=mysend).grid(column=1, row=1, sticky=(W,E))

# Listen for and connect to client socket
#name = input("Enter host name ")
s.connect((name,port))
s.settimeout(.5)

# Add a little space between widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Place cursor in the text entry and bind Enter key to the send as well
text_entry.focus()
root.bind("<Return>", mysend)

# Start idle receive loop
root.after_idle(myreceive, root)

# Start window loop
root.mainloop()