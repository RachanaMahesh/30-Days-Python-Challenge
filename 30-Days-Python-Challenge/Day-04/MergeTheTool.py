import textwrap
def merge_the_tools(string, k):
    # your code goes here
    wrapper = textwrap.TextWrapper(width=k)
    list = wrapper.wrap(text=string)
    # print(list)
    for s in list:
        c=''
        for i in range(k):
            if s[i] in c:
                continue
            c+=s[i]
        print(c)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)