def linear_search(li,ele):
    #li is the list & ele is the element to be searched.
    for i in range(len(li)):
        if li[i] == ele:
            return i
    return -1

li = [5, 10, 20, 40, 80]
index = linear_search(li,40)
print(index)