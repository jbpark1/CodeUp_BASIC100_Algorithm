'''
#방법 1
arr = [[]]
arr = [[0 for x in range(19)] for y in range(19)]

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

for i in range(19):
    for j in range(19):
        print(arr[i][j], end=' ')
    print()
'''
#방법 2
arr = []
for i in range(20):
    arr.append([])
    for j in range(20):
        arr[i].append(0)
        
n = int(input())
for i in range(n):
    x, y = input().split()
    arr[int(x)][int(y)] = 1
    
for i in range(1,20):
    for j in range(1,20):
        print(arr[i][j], end=' ')
    print()