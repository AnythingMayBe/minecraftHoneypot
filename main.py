import json
from quarry.net.server import ServerFactory, ServerProtocol
from twisted.internet import reactor

class Protocol(ServerProtocol):
    def packet_status_request(self, buff):
        print(f"Listening on: {self.connect_host}:{self.connect_port} Protocol: {self.protocol_mode} Address: {self.remote_addr}")

class Factory(ServerFactory):
    protocol = Protocol

factory = Factory()
factory.listen("127.0.0.1", 25565)
reactor.run()