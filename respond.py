import misc
class respondMap:
    respondMap = dict(["a"])

    def __init__(self):
        print(type(respondMap))
        self.respondMap = dict(misc.loadMap())
        print(type(respondMap))
        
    def print():
        return(respondMap)

    def addResponse(self, key, response):
        respondMap[key] = response
        print(respondMap[key])
        misc.saveMap(respondMap)

    def findResponse(key):
        try:
            return respondMap[key]
        except:
            return ""