
# Requried Libraby for File Organizer
import os
import shutil # for copy & paste

path = input("Enter the path: ")
files = os.listdir(path)

# Show files - Show level 1
'''for file in files:
    filename, extension = os.path.splitext(file)
    print(filename, extension)
'''
# Show files 
for file in files:
    filename, extention = os.path.splitext(file)
    extention = extention[1:] # . is 0th index, will take affer .
    # print(extention)
    
