import configparser, json

config = configparser.ConfigParser()
config.read('data/ini2jsonex.ini')
# print(x) # purrr filename

# ini -> dict
myDict = {section: dict(config.items(section)) for section in config.sections()} 
print(myDict)

# stuff i want to keep in dict
test = ['192.168.1.11', '192.168.1.12', '192.168.1.13']

# remove stuff if its IN the list, change "val in test" -> "val not in test"
myDict = {key:val for key, val in myDict["ipaddr"].items() if val in test}

print(f"Result: {myDict}" )
