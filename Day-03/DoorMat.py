# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
str = input().split()
n, m = int(str[0]),int(str[1])
c='.|.'
for i in range(1,n,2):
    print((c*i).center(m,'-'))
print("WELCOME".center(m,'-'))
for i in range(1, n, 2):
    print((c*(n-i-1)).center(m,'-'))