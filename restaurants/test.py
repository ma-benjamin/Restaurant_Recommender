import json

f = open('./zipcodes/07039.json')

data = json.load(f)
f.close()
print(data["restaurants"])
