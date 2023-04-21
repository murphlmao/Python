import configparser, json

class iniReader(configparser.ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d

config = configparser.ConfigParser()
config.read('data/ini2jsonex.ini') # read *filename. start from root directory

filedict = iniReader.as_dict(config)

# ALTERNATIVE WAY:
# ini -> dict (for each section, print section then things under it)
# filedict = {section: dict(config.items(section)) for section in config.sections()}
print(filedict) # purrrr

# device = key
# ip = value
# 'ipaddr' is a section header in the ini file.
new_dict = {device: {'ipaddress': ip} for device, ip in filedict['ipaddr'].items()} # ITTTTERate 
print(new_dict) 

# cool could be done here, but no i wanna add more data
# no more mr. nice murph >:(
for device, values in new_dict.items():
		device_type = 'compooter' # mayb some method to discover data types?!?
		values['type'] = device_type

y = json.dumps(new_dict, indent=4) # dump, like the truck, to json
print(y)

newfile = open('data/daaata.json', 'w')
newfile.write(y)
newfile.close()