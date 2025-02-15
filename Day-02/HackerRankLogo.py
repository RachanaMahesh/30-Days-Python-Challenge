# n = int(input("Enter the thickness"))
# c = 'H'
# for i in range(n):
#     print((c*i).rjust(n-1)+c+(c*i).ljust(n-1))
# for i in range(n+1):
#     print((c*n).center((n*2)-1)+(c*0).center((n*2)-1)+(c*n).center((n*2)-1))
# for i in range((n+1)//2):
#     print((c*(n*5)).center((n*6)-1))
# for i in range(n+1):
#     print((c*n).center((n*2)-1)+(c*0).center((n*2)-1)+(c*n).center((n*2)-1))
# for i in range(n):
#     print(((c*(n-i-1)).rjust(n-1)+c+(c*(n-i-1)).ljust(n-1)).rjust((n*6)-3))

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
