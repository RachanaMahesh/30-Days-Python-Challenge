# OS module : allows us to interact with the underlying system in several diffrerent ways like 1. we can navigate the file system, to get file info , lookup & change the environmental variables
import os
from datetime import datetime
# print(dir(os))
print(os.getcwd()) # to get the current working directory
os.chdir("C:/Users/User/Desktop") # to change the current working directory
print(os.getcwd())
print(os.listdir()) # to list all files & folders. u can pass the path as a string 

#to create a new folder there are 2 ways
# os.mkdir("OS-Demo-2")
os.makedirs("OS-Demo-2/Sub-Dir-1") # if u want to create a all of the intermediate directories that u need to make
print(os.listdir()) 

#to delete a new folder there are 2 ways
# os.rmdir("OS-Demo-2")
os.removedirs("OS-Demo-2/Sub-Dir-1")

# os.rename('test.txt','demo.txt')
# print(os.listdir())

# to print all the info of demo.txt file
print(os.stat('demo.txt'))
print(os.stat('demo.txt').st_ctime)

mod_time = os.stat('demo.txt').st_ctime
print(datetime.fromtimestamp(mod_time))

# to traverse the entire directory tree & files within the desktop
 # os.walk(): is a generator that yields a couple of 3 values as its walking the directory tree so for each directory that it sees,
#it yields the directory path, the directories within that path & the files within that path & by default it raverses from top to bottom 
for dirpath, dirnames, filenames in os.walk("C:/Users/User/Desktop"):
    print('Current Path : ', dirpath)
    print("DIrectories : ", dirnames)
    print("Files : ", filenames)
    print()
# it can be useful when say we have a file somewhere which we don't remember where it was then we could use this os.walk() to traverse through all the files & folder on the desktop
print("--------------------------------------------------------------------------------------------------------")

# Inorder to access home directory location by grabbing the home environmental variable 
print(os.environ.get('OneDrive'))
file_path = os.environ.get('OneDrive')+'test.txt' 
print(file_path) # C:\Users\User\OneDrivetest.txt : if we don't have '\' in environ then we need add it explicitly to avoid this we can use os.path

# os.path module has lot of useful but here we r using it to combine the home(OneDrive) directory with the file name 
# via os.path.join which joins 2 paths together
filepath = os.path.join(os.environ.get('OneDrive'),'test.txt')
print(filepath)
print("--------------------------------------------------------------------------------------------------------")


# NOTE : below path is fake path
print(os.path.basename('/tmp/test.txt')) # it will grab the file name of any path that we're working on & this doesn't have to be a real path
print(os.path.dirname('/tmp/test.txt')) # if u want the directory name of the path 
print(os.path.split('/tmp/test.txt')) # if u need both the name

print(os.path.exists('/tmp/test.txt'))# inorder to check if the given path is exist or not

print(os.path.isdir('/tmp/test.txt')) # we might have saved few files without extension so in that case we can use this to check if it is a directory or not

print(os.path.splitext('/tmp/test.txt')) # split the  root of the path & the extension

print(dir(os.path))