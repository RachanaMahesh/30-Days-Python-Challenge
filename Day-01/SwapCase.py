#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
s = 'Www.HackerRank.com'
r=''
for i in s:
    # print(i)
    if i.islower():
        r=r+i.upper()
    elif i.isupper():
        r=r+i.lower()
    else:
        r=r+i
print(r)