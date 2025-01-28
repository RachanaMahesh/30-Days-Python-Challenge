# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
# Scoring
# A player gets +1 point for each occurrence of the substring in the string .
# Output: the winner's name and score, separated by a space on one line, or Draw if there is no winner
def minion_game(string):
    n = len(string)
    stuartscore = 0
    kevinscore = 0
    for i in range(n):
        if string[i] in ('AEIOU'):
            kevinscore+=(n-i)
        else:
            stuartscore+=(n-i)
    print(stuartscore)
    print(kevinscore)
    if stuartscore > kevinscore:
        print("Stuart",stuartscore)
    elif kevinscore > stuartscore:
        print("Kevin",kevinscore)
    else:
        print("Draw")

    # --------------------------------------------
    # vowels = 'AEIOU'
    # stuartscore = 0
    # kevinscore = 0
    # n=len(string)
    # for i in range(n):
    #     if vowels.find(string[i]) != -1 :
    #         for j in range(i+1,n+1):
    #             # print(string[i:j])
    #             kevinscore+=1
    #     else:
    #         for j in range(i+1,n+1):
    #             # print(string[i:j])
    #             stuartscore+=1
    # print(stuartscore)
    # print(kevinscore)
    # if stuartscore > kevinscore:
    #     print("Stuart",stuartscore)
    # elif kevinscore > stuartscore:
    #     print("Kevin",kevinscore)
    # else:
    #     print("Draw")

if __name__ == '__main__':
    s = 'BANANA'
    # s = input()
    minion_game(s)