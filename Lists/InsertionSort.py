def InsertionSort(arr):
    length = len(arr)
    for i in range(1,length):
        j = i-1
        temp = arr[i]
        while(j>=0 and arr[j]>temp):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp

arr = [1,3,2,4,6,5,8,9,7,0,11]
InsertionSort(arr)
print(arr)