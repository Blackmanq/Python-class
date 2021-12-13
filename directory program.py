#import os library
import os

def info():
    file = input("filename:")
    Name = input("Name:")
    Adress = input("Address:")
    PN = input("Phone Number:")
    information = [Name, Adress, PN]
    saveFile = open(file, "a+")
    combined = "\n" + Name + "," + Adress + "," + PN
    saveFile.write(combined)
    contents = saveFile.read()
    print(combined)
    saveFile.close()
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

