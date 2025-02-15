string = "aaabbcddd"
str1=""
n= len(string)
c=1
for i in range(n-1):
    if string[i] == string[i+1]:
        c+=1
        continue
    str1 += string[i]+str(c)
    c=1
str1+= string[-1]+str(c)
print(str1)

