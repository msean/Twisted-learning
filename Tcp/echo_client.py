from twisted.internet import reactor,protocol


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("Hello World!".encode())

    def dataReceived(self, data):
        print("Server said:",data)
        self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self,addr):
        return EchoClient()

    def clientConnectFailed(self,connector,reason):
        print("conection failed")
        reactor.stop()

    def connectionLost(self, reason):
        print("conection lost")
        reactor.stop()

reactor.connectTCP("localhost",8000,EchoFactory())
reactor.run()