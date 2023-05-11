# Rectangular Star Pattern
'''For input n it will print n no. of rows
j will be the no. of columns'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
        print("*", end = '')
        j = j + 1
    print()
    i = i + 1