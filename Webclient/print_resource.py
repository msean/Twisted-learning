from twisted.internet import reactor
from twisted.web.client import getPage
import sys

def printPage(result):
    print(result)

def printError(failure):
    print(failure)

def stop(result):
    reactor.stop()


d = getPage(" http://www.baidu.com".encode())
d.addCallbacks(printPage, printError)
d.addBoth(stop)
reactor.run()