# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap

# def wrap(string, max_width):
#     str = ''
#     i=0
#     while i < len(string):
#         str += (string[i:i+max_width]+'\n')
#         i+=max_width
#     return str

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

def wrap(string, max_width):
    
    wrapper=textwrap.TextWrapper(width=max_width)
    s = wrapper.fill(text=string)
    
    
    return s