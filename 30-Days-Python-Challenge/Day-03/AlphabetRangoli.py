n = int(input())
alphabet = [chr(i) for i in range(97,123)][:n]
alphabet.reverse() # ['c','b','a']
h = n+(n-1)
w = h+(h-1)
for i in range(n):
    print(("-".join(alphabet[:i+1]+alphabet[:i][::-1])).center(w,'-'))
for i in range(n-1):
    print(("-".join(alphabet[:n-i-1]+alphabet[:n-i-2][::-1])).center(w,'-'))
# for i in range(1,n):
#     print("-".join(alphabet[:n-i]+alphabet[:n-i-1]).center(w,'-'))

