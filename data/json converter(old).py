from importlib.resources import path ; from pathlib import Path
import json, os, sys, shutil
 
#Input Json File Name
importedfile = input('Filename & Extention: ')
check = os.path.exists(importedfile)

if check is True:
    file = open(importedfile)
    data = json.load(file)
    print(data)
    file.close()
else:
    print('\033[1m' + 'File Does Not Exist! Check Spelling & Path')
    exit('\033[0m')

#Write New File With Parsed Dictionary To \Parsed Jsons\
save_path = 'Parsed Jsons'
completeName = os.path.join(save_path, importedfile+".txt")
print(completeName)

file1 = open(completeName, "w")
file1.write(str(data))
file1.close()

#Move Unparsed File to \Unparsed Jsons\
file_source = 'CURRENT FILE LOCATION'
file_destination ='WHERE YOU WANT FILE TO GO'

for file in Path(file_source).glob(importedfile):
    shutil.move(os.path.join(file_source,file),file_destination)

    #Suppress Output
class DevNull:
   def write(self, msg):
        pass

sys.stderr = DevNull()
