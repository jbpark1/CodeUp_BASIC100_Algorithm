a, d, n = map(int, input().split())

sum = a

for i in range(2, n+1):
    sum += d
print(sum)

# 1 4 7 10 13 16...
# 2 5 8 11 14 17...