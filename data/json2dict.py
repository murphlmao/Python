import json


openfile = open('data.json')

data = json.load(openfile)

print(data['camera1'])