# Given an integer, , print the following values for each integer  from  to :
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
n = int(input())
# for i in range(1,n+1):
#     print(i,oct(i)[2:],hex(i)[2:],bin(i)[2:])
width = len(format(n,'b'))
for i in range(1,n+1):
    print(f"{i:>{width}d} {i:>{width}o} {i:{width}X} {i:>{width}b}")
    # print(str(i).rjust(width," "),oct(i)[2:].rjust(width," "),hex(i)[2:].rjust(width," "),bin(i)[2:].rjust(width," "))
    # Notice the difference in the hexadecimal output (A vs. a):
    # The f-string uses X for uppercase hexadecimal.
    # The hex() function's default behavior is lowercase.
    
# is used for formatting numbers in different representations, with alignment and padding determined by the variables i and width. 
