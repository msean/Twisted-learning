from twisted.internet import reactor
from twisted.internet.task import deferLater
from twisted.web.resource import Resource
from twisted.web.server import Site, NOT_DONE_YET
import time

class BusyPage(Resource):
    isLeaf = True
    def _delayedRender(self, request):
        request.write(("Finally done, at %s" % (time.asctime(),)).encode())
        request.finish()

    def render_GET(self, request):
        d = deferLater(reactor, 5, lambda: request)
        d.addCallback(self._delayedRender)
        return NOT_DONE_YET

factory = Site(BusyPage())
reactor.listenTCP(8000, factory)
reactor.run()


# If you run Example  and then load multiple instances of http://
# localhost:8000 in a browser, you may still find that the requests are pro‐
# cessed serially. This is not Twisted’s fault: some browsers, notably
# Chrome, serialize requests to the same resource. You can verify that the
# web server isn’t blocking by issuing several simultaneous requests
# through cURL or a quick Python script.
