def BubbleSort(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(length-1-i):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
arr = [8,4,5,3,6,7,1,9,2,0]
BubbleSort(arr)
print(arr)