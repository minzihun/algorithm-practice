v = list(set([input() for _ in range(int(input()))]))
v.sort(key = lambda x:(-len(x),x))
print("\n".join(v)) 