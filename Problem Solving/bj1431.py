n=int(input())
guitar=[]
for _ in range(n):
    count=0
    command=input()
    for c in command:
        if c.isdigit():
            count+=int(c)
    guitar.append((command,count))
guitar.sort(key=lambda x : (len(x[0]), x[1], x[0]))

for g in guitar:
    print(g[0])