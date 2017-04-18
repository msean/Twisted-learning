import sys
from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent

class ResourcePrinter(Protocol):
    def __init__(self, finished):
        self.finished = finished

    def dataReceived(self, data):
        print(data)

    def connectionLost(self, reason):
        self.finished.callback(None)

def printResource(response):
    print(response)
    finished = Deferred()
    #Because the response is coming across the network in chunks, we need a Protocol that will
    #process the data as it is received and notify us when the body has been completely delivered.
    response.deliverBody(ResourcePrinter(finished))
    return finished
    # return response

def printError(failure):
    print("failure:",failure)

def stop(result):
    reactor.stop()

agent = Agent(reactor)
#request returns a Deferred that fires
#with a Response object encapsulating the response to the request
d = agent.request(b'GET',b'http://www.baidu.com')
d.addCallbacks(printResource, printError)
d.addBoth(stop)
reactor.run()
