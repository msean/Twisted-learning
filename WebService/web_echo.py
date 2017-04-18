from twisted.protocols import basic
from twisted.internet import protocol,reactor

class HTTPEchoRequest(basic.LineReceiver):

    def __init__(self):
        self.lines = []

    def lineReceived(self, line):
        self.lines.append(line)
        if not line:
            self.sendRequest()


    def byte_list_decode(self,blist):
        return [member.decode() for member in blist]

    def sendRequest(self):
        self.sendLine("HTTP/1.1 200 OK".encode())
        self.sendLine("".encode())
        print(self.lines)
        responseBody = "You said:\r\n\r\n" + "\r\n".join(self.byte_list_decode(self.lines))
        self.transport.write(responseBody.encode())
        self.transport.loseConnection()

class HTTPEchoFactory(protocol.ServerFactory):
    def buildProtocol(self, addr):
        return HTTPEchoRequest()


reactor.listenTCP(8000, HTTPEchoFactory())
reactor.run()
