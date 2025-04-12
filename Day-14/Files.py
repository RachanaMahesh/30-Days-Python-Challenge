import os
print(os.getcwd())

f = open("FileTest.txt",'r')
print(f.name)
print(f.mode)
f.close()

print("----------------via Context Manager 1. read()-------------------")
# with open("FileTest.txt",'r') as f:
    # pass
# print(f.read()) #ValueError: I/O operation on closed file.
    # f_content = f.read()
    # f_content = f.readline()
    # f_content = f.readlines() # return all the lines within a list
    # print(f_content, end="")
    
    # for line in f:
    #     print(line, end="")
    # print()

print("--------------------------------read(100)---------------------------------")
with open("FileTest.txt",'r', newline='') as f:
    print(f.tell())
    print(f.read(27))
    f.seek(5)
    print(f.read(27))
    print(f.tell()) # O/P: 18446744073709551639 to avoid this error add newline='' 
    # size_to_read = 20
    # f_content = f.read(size_to_read)
    # while len(f_content) > 0:
    #     print(f_content,end="**")
    #     f_content = f.read(size_to_read)

print("--------------------------------Write()---------------------------------")
# with open("FileTest2.txt",'w') as f:
#     # pass # not manadatory to write something inorder to create a file
#     f.write("Test")
#     f.write("Test")
#     f.seek(0)
#     f.write("R")

print("--------------------------------read() & Write()---------------------------------")
# with open("FileTest.txt",'r') as fr:
#     with open("FileTest_Copy.txt",'w') as fw:
#         for line in fr:
#             fw.write(line)

#  To read & write images we need to use mode as 'rb' & 'wb'
# with open("Rachu_Profile.jpg",'rb') as fr:
#     with open("Rachu_Profile_Copy.jpg",'wb') as fw:
#         for line in fr:
#             fw.write(line)

# sometimes u need more control on what are you reading & writing so instaed of doing it line by line we can do by specific chunck size.
with open("Rachu_Profile.jpg",'rb') as fr:
    with open("Rachu_Profile_Copy.jpg",'wb') as fw:
        chunk_size = 4036
        fr_chunk = fr.read(chunk_size)
        while len(fr_chunk ) > 0:
            fw.write(fr_chunk )
            file_content = fr.read(chunk_size)
            

    
    
    


