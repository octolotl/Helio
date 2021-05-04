# Helio
Bot I made for a friend's Discord server  

Prefix = o!  

It is used for setting a Minecraftserver's status manually and a custom rules and info command.  
To use the server status do these commands:  

Add your Discord id to the owners in the json file  
mcset - in the channel you want to put the server status  
setrole roleid - sets the role to ping when status changes  
ping on|off - sets if you want to ping the role or not  
setmessage - sends the message to be used for the server status  

Status commands:  
() = Optional  

on (reason)  
off (reason)  
restart (reason) | re (reason)  

Other commands:  
[] = Required  

messagechannel [message] | mc [message] - sends message to the channel you have set  
custom [message] | c [message] - sends a custom embed message  
rules [message] - sends a custom embed message with rules image at top  
