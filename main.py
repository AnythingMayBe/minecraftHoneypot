import json
from quarry.net.server import ServerFactory, ServerProtocol
from twisted.internet import reactor

class Protocol(ServerProtocol):
    def packet_status_request(self, buff):
        print(f"PING | Listening on: {self.connect_host}:{self.connect_port} Protocol: {self.protocol_version} Address: {self.remote_addr}")

    def packet_login_start(self, buff):
        buff.discard()
        print(f"JOIN | Listening on: {self.connect_host}:{self.connect_port} Protocol: {self.protocol_version} Address: {self.remote_addr}")
        self.close("bye")


class Factory(ServerFactory):
    protocol = Protocol

factory = Factory()
factory.listen("127.0.0.1", 25565)
reactor.run()