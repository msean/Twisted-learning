from twisted.internet import protocol,reactor


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        print("Got client data:",data.decode())
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

reactor.listenTCP(8001, EchoFactory())
reactor.run()



