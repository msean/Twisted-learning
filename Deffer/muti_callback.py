from twisted.internet.defer import Deferred

def addBold(result):
    return "<b>%s</b>" % (result)

def addItalic(result):
    return "<b>%s</b>" % (result)

def printHtml(result):
    print(result)


d = Deferred()
d.addCallback(addBold)
d.addCallback(addItalic)
d.addCallback(printHtml)
d.callback("Hello World")
