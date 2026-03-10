import json

FILENAME = "testdict.json"

def readDict():
    with open(FILENAME) as f:
        return json.load(f)
    
# test
somedict = readDict()
print(somedict)