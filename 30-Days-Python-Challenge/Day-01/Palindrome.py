#Given a string. the task is to check if the string is symmetrical and palindrome or not. 
# A string is said to be symmetrical if both the halves of the string are the same and a string is said to be a palindrome string 
# if one half of the string is the reverse of the other half or if a string appears the same when read forward or backward.
def palindrome(s):
    return s[::-1]

def symmetrical(s):
    mid = len(s)//2
    if len(s)%2 == 0:
        return s[:mid] == s[mid:]
    else:
        return s[:mid] == s[mid+1:]
    
strg = input("Enter the string:")
if strg == palindrome(strg):
    print("The entered string is palindrome")
else:
    print("The entered string is NOT a palindrome")
if symmetrical(strg):
    print("The entered string is symmetrical")
else:
    print("The entered string is Not symmetrical")
