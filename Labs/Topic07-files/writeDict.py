import json

FILENAME = "testdict.json"

sample = dict(name="fred", age=31, grades=[1,54,66])

def writeDict(obj):
    with open(FILENAME, "wt") as f:
        json.dump(obj, f)

# test
writeDict(sample)