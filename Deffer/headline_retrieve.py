from twisted.internet import reactor,defer

class HeadLineRetrieve(object):

    def processHeadLine(self,headline):
        print(headline)
        if len(headline) > 50:
            self.d.errback("The headline '%s' is too long"%(headline))
        else:
            self.d.callback(headline)

    def _toHtml(self,result):
        return "<h1>%s</h1>"%(result)

    def getHeadLine(self,input):
        self.d = defer.Deferred()
        reactor.callLater(2,self.processHeadLine,input)
        self.d.callback(self._toHtml)
        return self.d

def printData(result):
    print("result",result)
    reactor.stop()

def printError(failure):
    print("failure",failure)
    reactor.stop()

h = HeadLineRetrieve()
d = h.getHeadLine("Breaking News:Twisted Takes Us to the Moon")
d.addCallbacks(printData,printError)

reactor.run()
