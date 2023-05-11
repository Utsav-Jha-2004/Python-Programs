str = input().split()
n,m = int(str[0]),int(str[1])
li = [[int(j) for j in input().split()] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(li[i][j], end = ' ')
    print()