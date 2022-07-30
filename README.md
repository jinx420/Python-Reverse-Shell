# Attention
This Repo is intended for educational purposes only. I cant be held liable for any damages 
caused by improper usage of this publication.

# Works on Linux as well as Windows

# Client.py or Client.pyw?
Client.py is more of a debug version because it shows the terminal when you open it so choose Client.pyw (Client.pyw only works on Windows)

# Outside of local Network
If you want it to work outside of your local network then edit RevShellServer.py and follow the instructions do the same with Client.py and/or Client.pyw

# New Issues
If you encounter any Issues make sure to open a new Issue under the 'Issues' tab and I will try to fix it as soon as possible

# Common issues
Why doesnt it run
- Python needs to be installed for it to work duh

I have python installed but it doesnt run
- Check if you have all the packages installed but every package should already be installed

It wont connect
- There can be many reasons for that, but most common are: firewall blocking traffic (this is only an issue when you use it outside of your local Network), the port on which the Server runs is already used (this will output an error saying that the port is already in use, change it if thats the case)

I opened a file through the reverse shell now i cant do anything
- You cant open files through the reverse shell well technically you can but this breaks the shell since its waiting for a response

I created a file through it but i cant edit the file
- Use echo 'your text here' > filename or if you have multiple lines in that file echo 'your text here' >> filename

# Which commands work
Every command from the Terminal or Command prompt will work

# Can I add my own commands
Yes you can, follow the instruction in Client.py and RevShellServer.py
