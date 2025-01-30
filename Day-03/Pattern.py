s = 'PYTHON'
n = len(s)
# print("Pattern 1")
# for i in range(n):
#     for j in range(i+1):
#       print(s[i],end="")
#     print()
# print("------------------------------------------------")
# print("Pattern 2")
# for i in range(n):
#     print(((s[i])*(i+1)).rjust(n,' '))
# print("------------------------------------------------")
# print("Pattern 3")
# for i in range(n):
#     for j in range(i+1):
#       print(s[j],end="")
#     print()
# print("------------------------------------------------")
# print("Pattern 4")
# for i in range(n):
#     print((s[:i+1]).rjust(n,' '))
# print("------------------------------------------------")
# print("Pattern 5")
# for i in range(n):
#    print(' '.join((s[:i+1])).center((n*2-1),' '))

# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end='')
#     for j in range(i+1):
#         print(s[i],end=' ')
#     print()
# print("------------------------------------------------")
# print("Pattern 6")
# for i in range(n):
#     for j in range(i+1):
#         print(s[j],end=' ')
#     print()

# for i in range(n):
#     for j in range(n-i):
#         print(s[j],end=' ')
#     print()
# print("------------------------------------------------")
# print("Pattern 7")
# for i in range(n):
#     for j in range(i+1):
#         print(s[i],end=' ')
#     print()

# for i in range(n):
#     for j in range(n-i):
#         print(s[i],end=' ')
#     print()
# print("------------------------------------------------")
# print("Pattern 8")
# for i in range(n):
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(n-i):
#         print(s[j],end=' ')
#     print()
# for i in range(n):
#     print((s[:n-i]).rjust(n,' '))
# print("------------------------------------------------")
# print("Pattern 9")
# for i in range(n):
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(n-i):
#         print(s[i],end=' ')
#     print()
# print("------------------------------------------------")
# print("Pattern 10")
# for i in range(n):
#     for j in range(n-i):
#         print(s[j],end=' ')
#     print()
#     for j in range(i+1):
#         print(" ",end='')
# print("OR")
# for i in range(n):
#     print(" ".join((s[:n-i])).center((n*2-1),' '))
# print("------------------------------------------------")
# print("Pattern 11")
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(n-i):
#         print(s[i],end=" ")
#     print()
# print("------------------------------------------------")
# print("Pattern 12")
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end=' ')
    for j in range(i+1):
        print(s[i],end=" ") 
    print()   
# print("------------------------------------------------")
# print("Pattern 13")
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end=' ')
    for j in range(i,-1,-1):
        print(s[j],end=" ") 
    print()