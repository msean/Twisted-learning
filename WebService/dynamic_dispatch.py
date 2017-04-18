from twisted.internet import reactor
from twisted.web.resource import Resource, NoResource
from twisted.web.server import Site
from calendar import calendar

class YearPage(Resource):
    def __init__(self, year):
        Resource.__init__(self)
        self.year = year

    def render_GET(self, request):
        return ("<html><body><pre>%s</pre></body></html>" % (calendar(self.year),)).encode()

class CalendarHome(Resource):

    isLeaf = False

    def getChild(self, name, request):
        name = name.decode()
        if name == '':
            # from datetime import datetime
            # from twisted.web.util import redirectTo
            # return redirectTo((datetime.now().year), request)
            return self
        if name.isdigit():
            return YearPage(int(name))
        else:
            return NoResource()

    def render_GET(self, request):
        return ("<html><body>Welcome to the calendar server!</body></html>").encode()

#
# class ClockPage(Resource):
#     isLeaf = True
#
#     def render_GET(self, request):
#         return ("The local time is %s" % (time.ctime(),)).encode()
        # return ("<html><body>Welcome to the calendar server!</body></html>").encode()

resource = CalendarHome()
factory = Site(resource)
reactor.listenTCP(8000, factory)
reactor.run()


# resource = CalendarHome()
# factory = Site(resource)
#
# reactor.listenTCP(8000, factory)
# reactor.run()

