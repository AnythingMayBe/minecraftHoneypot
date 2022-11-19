# Minecraft Honey Pot
A simple Python script that will try to create a Minecraft server on specific ports, and blacklists everyone that tries to connect on that port.

# Config
The first two options are available for blacklisting IPs that tries to connect. You can edit the blacklist command on the main.py file.
```json
    "blacklistJoin": true,
    "blacklistPing": true,
```

The next two options have specific meaning for each of them. The webhook option is for alerting you on a Discord-webhook based schema, and the disconnectReason option is the reason for kicking players that tries to connect.
```json
    "webhook": "",
    "disconnectReason": "bye",
```

The ports option is the list of ports that our script should listen to. The list we have is based on some lists used by hackers that I got access to.