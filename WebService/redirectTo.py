from datetime import datetime
from twisted.web.util import redirectTo
from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
import time


class ClockPage(Resource):
    isLeaf = True

    def render_GET(self, request):
        return redirectTo(datetime.now().year, request)
        # return ("<html><body>Welcome to the calendar server!</body></html>").encode()

resource = ClockPage()
factory = Site(resource)
reactor.listenTCP(8000, factory)
reactor.run()
