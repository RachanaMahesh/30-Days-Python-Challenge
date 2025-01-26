# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
if __name__ == '__main__':
    s = input()
    print(any(ch.isalnum() for ch in s ))
    print(any(ch.isalpha() for ch in s ))
    print(any(ch.isnumeric() for ch in s))
    print(any(ch.islower() for ch in s))
    print(any(ch.isupper() for ch in s))

    
# using regex:

import re

if __name__ == '__main__':
    s = input()
    print(True if re.search(r'[a-zA-Z0-9]', s) else False)
    print(True if re.search(r'[a-zA-Z]', s) else False)
    print(True if re.search(r'[0-9]', s) else False)
    print(True if re.search(r'[a-z]', s) else False)
    print(True if re.search(r'[A-Z]', s) else False)