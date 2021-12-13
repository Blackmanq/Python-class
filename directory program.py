#import os library
import os

def info():
    file = input("filename:")
    Name = input("Name:")
    Adress = input("Address:")
    PN = input("Phone Number:")
    saveFile = open(file, "w")
    saveFile.write(f"{Name},{Adress},{PN}")
    file_contents = saveFile.read()
    print(file_contents)
    return


#inputvariables
destination = input("Directory You'd like to save to:")
filename = input("File Name:")

#check if directory exists if so create file
if(os.path.exists(destination)):
    open(filename,"w+")
    os.popen(f"copy {filename}  {destination}")
    info()
else:
    print("Directory does not exist")

