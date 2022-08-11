import misc
class respondMap:
    respondMap = dict()
    print(type(respondMap))

    def __init__(self):
        respondMap = dict()
        print(type(respondMap))
        self.respondMap = dict(misc.loadMap())
        print(type(respondMap))
        
    def print():
        return(respondMap)

    def addResponse(self, key, response):
        respondMap = misc.loadMap()
        print(type(respondMap))
        respondMap[key] = response
        print(respondMap[key])
        try:
            misc.saveMap(respondMap)
            return("Saved " + str(response) + " at " + str(key))
        except:
            return ""

    def findResp(self, key):
        try:
            return respondMap[key]
        except:
            return ""