n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

for i in range(n-1,-1,-1):     #역순일땐 증가폭(-1) 지정이 필요
    print(a[i], end=' ')