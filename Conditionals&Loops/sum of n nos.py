# Given an integer n, find the sum from 1 to n.
n = float(input())
count = 1
sum = 0
while count <= n:
    sum = sum + count
    count = count + 1
print(sum)