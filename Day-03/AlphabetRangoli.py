n = 3
alphabet = [chr(i) for i in range(97,123)][:n]
alphabet.reverse() # ['c','b','a']
w = n+(n-1)
w += (w-1)
for i in range(n):
    print(alphabet[i-1:0:-1])
    #print(alphabet[:i+1])