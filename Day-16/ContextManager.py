# Context Manager allow us to properly manage resources so that we can specify exactly what we want to set up & tear down when working with certain objects. No need to remember to close the file when we use context manager(with)
# Eg: used to connect & close database automatically, we can aquire & release locks etc

# f = open("TestSample.txt",'w')
# f.write("1. This is the statement to test")
# f.close()

# with open("TestSample.txt",'w') as f:
#     f.write("2. This is the statement to test")

print("------------------ Using class for Custom Context Manager  ------------------------------------------")
# class Open_file:
#     def __init__(self,filename, mode):
#         self.filename = filename
#         self.mode = mode
    
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
    
#     def __exit__(self,exc_type, exc_val, traceback):
#         self.file.close()

# with Open_file("TestSample.txt",'w') as f:
#     f.write("3. This is the statement to test")

# print(f.closed)

print("------------------ Using Function for Custom Context Manager via decorators  ------------------------------------------")
from contextlib import contextmanager

# @contextmanager
# def open_file(filename,mode):
#     file = open(filename,mode)
#     yield file
#     file.close()

# with open_file("TestSample.txt",'w') as f:
#     f.write("4. This is the statement to test")
# print(f.closed)

print("-------------- Using Try & finally blosk to handle errors in Function for Custom Context Manager via decorators  ----------------")
# @contextmanager
# def open_file(filename,mode):
#     try:
#         file = open(filename,mode) # open is already a context manager in python we can do everything we did using open() function alone        
#         yield file
#     finally:
#         file.close()

# with open_file("TestSample.txt",'w') as f:
#     f.write("4. This is the statement to test")
# print(f.closed)

# As open is already a context manager in python, so we can replicate open func using both class & func based & refer practile example below
import os

# cwd = os.getcwd()
# os.chdir('Day-15')
# print(os.listdir())
# os.chdir(cwd)

# cwd = os.getcwd()
# os.chdir('Day-14')
# print(os.listdir())
# os.chdir(cwd)

@contextmanager
def changedir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination) # we r not working with variables/objects inside context manager so no need to yield anything
        yield
    finally:
        os.chdir(cwd)

with changedir('Day-15'): # as we not working on any variables we can skip as f
    print(os.listdir())

with changedir('Day-14'): # as we not working on any variables we can skip as f
    print(os.listdir())