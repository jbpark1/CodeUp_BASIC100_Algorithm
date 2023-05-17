h, w = map(int, input().split())

arr = []
arr = [[0 for x in range(w+1)] for y in range(h+1)] # w, h 위치 주의
#arr=[[0]*w for _ in range(h)]

'''
for i in range(h):
    for j in range(w):
        print(j, end=' ')
        #print(arr[i+1][j+1], end = ' ')
    print()
'''

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    
    for j in range(l):
        
            if d==0: #가로
                arr[x-1][y-1+j]=1
            else:    #세로
                arr[x-1+j][y-1]=1
    
#출력
for i in range(h):
    for j in range(w):
        #print(j, end=' ')
        print(arr[i][j], end=' ')
    print()