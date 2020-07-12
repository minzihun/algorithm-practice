def insertion_sort(arr):
    for end in range(1,len(arr)):
        for i in range(end, 0 , -1):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                
a=[1,10,5,8,7,6,4,3,2,9]
print(a)
insertion_sort(a)
print(a)                