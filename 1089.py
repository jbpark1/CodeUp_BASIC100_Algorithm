a, r, n = map(int, input().split())

sum = a

for i in range(2, n+1):
    sum*=r
print(sum)