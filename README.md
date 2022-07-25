# Attention
This Repo is intended for educational purposes only. I cant be held liable for any damages 
caused by improper usage of this publication.

# Works on Linux as well as Windows

# Client.py or Client.pyw?
Client.py is more of a debug version because it shows the terminal when you open it so choose Client.pyw (client.pyw only works on linux)

# Outside of local Network
If you want it to work outside of your local network then edit RevShellServer.py and follow the instructions do the same with Client.py or Client.pyw

# Common issues
Why doesnt it run?
- Python needs to be installed for it to work duh

I have python installed but it doesnt run
- Check if you have all the packages installed but every package should already be installed

It wont connect
- There can be many reasons for that most common are: firewall blocking traffic (this is only an issue when you use it outside of your local Network), the port on which the Server runs is already used (this will output an error saying that the port is already in use, change it if thats the case)

# Which commands work
Every command from the Terminal or Command prompt will work

# Can I add my own commands
Yes you can do it like this:

Add this code at line 23 or below (Client.py)

Add this code at line 30 or below (RevShellServer.py)

if cmd.lower() in ['command alias', 'command']:
  
  put your code here and change comamnd alias with your alias and command with the full name of your command and make sure to add the command to both the client and server
 
