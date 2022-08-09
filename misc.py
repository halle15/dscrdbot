from logging import exception
import pickle


def retKey():
    with open("key.txt") as f:
        return f.readline()

def loadMap():
    with open("responsemap", "rb") as f:
        try:
            return dict(pickle.load(f))
        except Exception as e:
            print(e)
            print("Error with map load, returning error:error map")
            return {"error" : "error"}

def saveMap(map):
    with open("responsemap", "wb") as f:
        try:
            print("saved")
            pickle.dump(map, f, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            print(e)
            print("Error with map save")
            return
