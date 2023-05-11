def large_col_sum(li):
    n = len(li)
    m = len(li[0])
    
    max_sum = -1
    max_col_index = -1
    for j in range(m):
        sum = 0
        for ele in li:
            sum += ele[j]
        if sum > max_sum:
            max_col_index = j
            max_sum = sum
    return max_sum, max_col_index

li = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
max_sum,max_col_index = large_col_sum
print(max_sum, max_col_index)