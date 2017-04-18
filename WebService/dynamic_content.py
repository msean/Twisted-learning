from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
import time

class ClockPage(Resource):
    isLeaf = True

    def render_GET(self, request):
        return ("The local time is %s" % (time.ctime(),)).encode()
        # return ("<html><body>Welcome to the calendar server!</body></html>").encode()

resource = ClockPage()
factory = Site(resource)
reactor.listenTCP(8000, factory)
reactor.run()

#if visit localhost:8000/ return the