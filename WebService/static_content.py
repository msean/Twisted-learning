from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

resource = File('/home/mwh/ad_django/static/images')
factory = Site(resource)
reactor.listenTCP(8000, factory)

reactor.run()

#http://192.168.1.229:8000/prod2.jpg