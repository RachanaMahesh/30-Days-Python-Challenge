string = "ABCD"
def permutation(string,step=0):
    if step == len(string):
        print(''.join(string))
        return
    for i in range(step,len(string)):
        string_copy = [c for c in string]
        string_copy[step],string_copy[i] = string_copy[i], string_copy[step]
        permutation(string_copy,step+1)
    
permutation(string)
