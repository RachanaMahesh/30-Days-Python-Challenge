if __name__ == '__main__':
    N = int(input())
    arr = []
    str =[]
    for i in range(N):
        arr.append(input().split())
    for i in range(len(arr)):
        str[i] = arr[i]
        print(str)
        if str[i][0] == 'insert':
            arr.insert(int(str[i][1]),int(str[i][2]))
        elif str[i][0]  == 'print':
            print(arr)
        elif str[i][0]  == 'append':
            arr.append(int(str[i][1]))
        elif str[i][0]  == 'remove':
            arr.remove(int(str[i][1]))
        elif str[i][0]  == 'sort':
            arr.sort()
        elif str[i][0]  == 'pop':
            arr.pop()
        elif str[i][0] == 'reverse':
            arr.reverse()