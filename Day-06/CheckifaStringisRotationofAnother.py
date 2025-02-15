str1 = "waterbottle"
str2 = "erbottlewat"
n=len(str1)
count=0
if len(str1) == len(str2):
    for i in range(len(str1)):
        str1=str1[-1]+str1[:n-1]
       # print(str1)
        if str1 == str2:
            count+=1
            break
    if count > 0:
        print("True")
    else:
        print("False")
else:
    print("False")