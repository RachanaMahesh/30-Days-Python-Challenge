n = int(input("Enter the thickness"))
c = 'H'
for i in range(n):
    print((c*i).rjust(n-1)+c+(c*i).ljust(n-1))