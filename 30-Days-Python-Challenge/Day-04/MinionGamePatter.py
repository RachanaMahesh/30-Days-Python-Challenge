def minion_game(string):
    stuartlist=[]
    kevinlist = []
    stuartscore = []
    kevinscore = []
    n=len(string)
    for i in range(n):
        if string[i] in ('AEIOU'):
            for j in range(i+1,n+1):
                # print(string[i:j])
                if string[i:j] in kevinlist:
                    kevinscore+=1
                    continue
                kevinlist.append(string[i:j])
                kevinscore+=1
        else:
            for j in range(i+1,n+1):
                # print(string[i:j])
                if string[i:j] in stuartlist:
                    stuartscore+=1
                    continue
                stuartlist.append(string[i:j])    
                stuartscore+=1
    print(stuartscore)
    print(kevinscore)


if __name__ == '__main__':
    s = 'BANANA'
    # s = input()
    minion_game(s)