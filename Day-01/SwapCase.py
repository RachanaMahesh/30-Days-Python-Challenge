#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
s = 'Www.HackerRank.com'
r=''
for i in range(len(s)):
    if s[i].islower():
        r=r+s[i].upper()
    elif s[i].isupper():
        r=r+s[i].lower()
    else:
        r=r+s[i]
print(r)