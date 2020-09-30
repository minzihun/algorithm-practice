n = int(input())
a = input().split()
arr = [0 for _ in range(24)]

for i in range(n) :
    arr[int(a[i])]+=1

for i in range(1, 24) :
    print(arr[i], end = " ")