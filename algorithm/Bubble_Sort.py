#-*- coding:utf-8 -*-
#Bubble Sort

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

a=[1,10,5,8,7,6,4,3,2,9]
print(a)
bubble_sort(a)
print(a)