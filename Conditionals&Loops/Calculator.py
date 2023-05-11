'''Calculator
1 = Sum
2 = Difference
3 = Product
4 = Quotient
5 = Remainder'''
while (True):
    ch = int(input())
    if (ch == 1):
        a = float(input())
        b = float(input())
        c = a+b
        print(c)
    elif (ch == 2):
        a = float(input())
        b = float(input())
        c = a-b
        print(c)
    elif (ch == 3):
        a = float(input())
        b = float(input())
        c = a*b
        print(c)
    elif (ch == 4):
        a = float(input())
        b = float(input())
        c = a//b
        print(c)
    elif (ch == 5):
        a = float(input())
        b = float(input())
        c = a%b
        print(c)
    else:
        print("Invalid Operation")