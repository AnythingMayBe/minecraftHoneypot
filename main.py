import json
from quarry.net.server import ServerFactory, ServerProtocol
from twisted.internet import reactor
import requests
from twisted.internet.error import CannotListenError
from os import system

# Base
def jsonloads():
    with open("config.json", "r") as file:
        global config
        config = json.loads(file.read())
        file.close()

def blacklist(ip, type):
    if config[f"blacklist{type}"] == True:
        system("iptables -A INPUT -s " + str(ip).split(", '")[1].split("', ")[0] + " -j DROP")

# Webhook request
def sendAlert(message):
    if config["webhook"] != "": # If you want to disable the webhook alert, simply change the webhook parameter to ''
        data = {"content": message}
        
        try:requests.post(config["webhook"], data=data)
        except requests.exceptions.ConnectionError: print("Invalid Domain name parsed. Make sure you don't have any spaces.")

    else: print(message)

# Quarry
class Protocol(ServerProtocol):
    def packet_status_request(self, buff):
        sendAlert(f"PING | Listening on: {self.connect_host}:{self.connect_port} Protocol: {self.protocol_version} Address: {self.remote_addr}")
        blacklist(self.remote_addr, "Ping")

    def packet_login_start(self, buff):
        buff.discard()
        sendAlert(f"JOIN | Listening on: {self.connect_host}:{self.connect_port} Protocol: {self.protocol_version} Address: {self.remote_addr}")
        self.close(config["disconnectReason"])
        blacklist(self.remote_addr, "Join")


class Factory(ServerFactory):
    protocol = Protocol

# Start
if __name__ == "__main__":
    jsonloads()
    factory = Factory()
    
    # Ports
    for port in config["ports"]:
        try: factory.listen("127.0.0.1", port=port)
        except CannotListenError as e: print(str(e))
        except Exception as e: print("Exception while trying to listen on " + str(port) + ": " + str(e))
    
    # Run
    reactor.run()