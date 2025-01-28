# You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
#  For example, alison heck should be capitalised correctly as Alison Heck.
# Input (stdin)
# 132 456 Wq  m e
# Expected Output
# 132 456 Wq  M E

def solve(s):
    count= 0 
    finalstr = ''
    for i in range(len(s)):
        if count==0 and s[i] != " ":
            # s[i]=s[i].capitalize
            finalstr+=(s[i].upper())
            count = 1
        elif s[i] == " ":
            count = 0
            finalstr+=s[i]
        else:
            finalstr+=s[i]
            count=1

    return finalstr
            
        #print(finalstr) return finalstr
    # w=[]
    # for i in s.split():
    #     w.append(i.capitalize())

    # return " ".join(w)
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)