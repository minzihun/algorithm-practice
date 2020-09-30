r, g, b = map(int, input().split())
count = 0
for rr in range(r) :
    for gg in range(g) :
        for bb in range(b) :
            print(rr, gg, bb)
            count+=1
print(count)