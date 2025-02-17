import string


class Solution:
    def dataTypeSize(self, str):
        # Code here
        if str == 'Integer':
            return int._sizeof_()
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str = input()
        ob = Solution()
        res = ob.dataTypeSize(str)
        print(res)
        print("~")
# } Driver Code Ends