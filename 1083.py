r, g, b = map(int, input().split())

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, end=' ')
            print(j, end=' ')
            print(k)
print(r*g*b)