def SelectionSort(arr):
    length = len(arr)
    for i in range(length - 1):
        minIndex = i
        for j in range(i+1, length):
            if(arr[j] < arr[minIndex]):
                minIndex = j
        arr[i],arr[minIndex] = arr[minIndex], arr[i]
    
arr = [5,4,3,0,8,9,1,7,6,2]
SelectionSort(arr)
print(arr)