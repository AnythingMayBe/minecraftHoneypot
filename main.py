import json
from quarry.net.server import ServerFactory, ServerProtocol
from twisted.internet import reactor

class Protocol(ServerProtocol): pass

class Factory(ServerFactory):
    protocol = Protocol

factory = Factory()
factory.listen("127.0.0.1", 25565)
reactor.run()