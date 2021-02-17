import os

DIR = os.getcwd()


def IsPNG(filename):
    with open(filename+".jpg", "r") as file:
        row = file.readline()
        if "PNG" in row:
            return True
        else:
            return False
         
         
def RenameJPGToPNG(filename):
    os.rename(filename+".jpg", filename+".png")
    
    
def RenameIfPNG(filename):
    if IsPNG(filename):
        print(filename+"is Renamed!")
        RenameJPGToPNG(filename)
  
  
def GetAllJPGs(directory):
    file_list = list()
    files = os.listdir(directory)
    for file in files:
        if ".jpg" in file:
            file_list.append(file)
    return file_list
    
    
def RenameFilesToOriginalFormat(directory):
    for file in GetAllJPGs(directory):
        filename = file.split(".jpg")[0]
        RenameIfPNG(filename)

RenameFilesToOriginalFormat(DIR)
