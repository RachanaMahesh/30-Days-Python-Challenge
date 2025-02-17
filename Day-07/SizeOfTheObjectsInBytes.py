import sys

# SIzE OF THE DATA OBJECT IN BYTES
class Solution:
    def dataTypeSize(self, string):
        # Code here
        # if str == 'Integer':
        #     return sys.getsizeof(int)
        dictionary = {
            'Integer' : int ,
            'Character' : str ,
            'Long' : int,
            'Float' : float

        }

        if string in dictionary:
            return sys.getsizeof(dictionary[string])
        else:
            return -1

        

#{ Character, Integer, Long, Float and Double
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