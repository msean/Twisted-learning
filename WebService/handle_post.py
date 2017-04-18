from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
import cgi


class FormPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        return  ("""
        <html>
            <body>
                <form method="POST">
                    <input name="form-field" type="text" />
                    <input type="submit" />
                </form>
            </body>
        </html>
        """).encode()

    def render_POST(self, request):
        return ("""
                <html>
                    <body>You submitted: %s</body>
                </html>
                """ % (cgi.escape((request.args[b"form-field"][0]).decode()))
             ).encode()

factory = Site(FormPage())
reactor.listenTCP(8000, factory)
reactor.run()