from twisted.internet.defer import Deferred


def callback1(result):
    print("Callback 1 said:",result)
    return result

def callback2(result):
    print("callback 2 said:",result)

def callback3(result):
    raise Exception("Callack3")

def errback1(failure):
    print("errback 1 had an error on",failure)
    return failure

def errback2(failure):
    raise Exception("Errback2")

def errback3(failure):
    print("Errback 3 took care of",failure)
    # return Exception("Everything is fine now")

# d = Deferred()
# d.addCallback(callback1)
# d.addCallback(callback2)
# d.callback("Test")


# d = Deferred()
# d.addCallback(callback1)
# d.addCallback(callback2)
# d.addCallback(callback3)
# d.addErrback(errback3)
# d.callback("Test")

d = Deferred()
d.addErrback(errback1)
d.errback(Exception("except"))