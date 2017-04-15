from twisted.internet.defer import Deferred,failure
from twisted.internet import error

class Err(Exception):
    def __str__(self):
        return "Err"

def myErrback(fail):
    print(fail.getBriefTraceback())


d = Deferred()
d.addErrback(myErrback)
d.errback(failure.Failure(Err()))