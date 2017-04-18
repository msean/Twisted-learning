from twisted.internet import reactor
from twisted.web import http

class myRequestHandler(http.Request):

    resources = {
        b'/': b'<h1>Home</h1>Home page',
        b'/about': b'<h1>About</h1>All about me',
    }

    def process(self):
        print("A request come:",self.path)
        self.setHeader('Content-Type'.encode(), 'text/html'.encode())
        if self.path in self.resources:
            self.write(self.resources[self.path])
        else:
            self.setResponseCode(http.NOT_FOUND)
            self.write("<h1>Not Found</h1>Sorry, no such resource.".encode())
        self.finish()

class MyHTTP(http.HTTPChannel):
    requestFactory = myRequestHandler

class MyHTTPFactory(http.HTTPFactory):
    protocol = MyHTTP

reactor.listenTCP(8000, MyHTTPFactory())
reactor.run()
