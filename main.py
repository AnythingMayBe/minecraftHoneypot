import json
from quarry.net.server import ServerFactory, ServerProtocol
from twisted.internet import reactor
import requests

# Base
def jsonloads():
    with open("config.json", "r") as file:
        global config
        config = json.loads(file.read())
        file.close()

# Webhook request
def sendAlert(message):
    if config["webhook"] != "": # If you want to disable the webhook alert, simply change the webhook parameter to ''
        data = {"content": message}
        requests.post(config["webhook"], data=data)
    else: print(message)

# Quarry
class Protocol(ServerProtocol):
    def packet_status_request(self, buff):
        sendAlert(f"PING | Listening on: {self.connect_host}:{self.connect_port} Protocol: {self.protocol_version} Address: {self.remote_addr}")

    def packet_login_start(self, buff):
        buff.discard()
        sendAlert(f"JOIN | Listening on: {self.connect_host}:{self.connect_port} Protocol: {self.protocol_version} Address: {self.remote_addr}")
        self.close("bye")


class Factory(ServerFactory):
    protocol = Protocol

# Start
if __name__ == "__main__":
    jsonloads()
    factory = Factory()
    factory.listen("127.0.0.1", 25565)
    reactor.run()