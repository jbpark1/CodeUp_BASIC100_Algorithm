
# 19*19 2차원 배열 선언 및 0으로 초기화 - 방법 1
arr = []
arr = [[0 for x in range(20)] for y in range(20)]

# 19*19 2차원 배열 선언 및 0으로 초기화 - 방법 2
# arr = []
# for i in range(4):
#    arr.append([])
#    for j in range(4):
#        arr.append(0)

# 19*19 배열 입력 받음
for i in range(19):
    a = input().split()                 # 19줄x19번 입력
    for j in range(19):
        arr[i+1][j+1] = int(a[j])       # 배열에 넣음
        

#몇 개의 좌표를 받을 것인지
n = int(input())

for i in range(n):
    x, y = map(int, input().split())    # n개 좌표 입력 -> 1부터 시작
    
    for j in range(1,20):
        if arr[x][j]==0:
            arr[x][j]=1
        else:
            arr[x][j]=0
        
        if arr[j][y]==0:
            arr[j][y]=1
        else:
            arr[j][y]=0

for i in range(1,20):
    for j in range(1,20):
        print(arr[i][j], end=' ')
    print()

''' 모범 답안
d=[]
d=[[0 for x in range(4)] for y in range(4)]

for i in range(3) :
  a = input().split()
  for j in range(3) :
    arr[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n) :
  x,y=input().split()
  x=int(x)
  y=int(y)
  for j in range(1, 4) :
    if arr[j][y]==0 :
      arr[j][y]=1
    else :
      arr[j][y]=0

    if arr[x][j]==0 :
      arr[x][j]=1
    else :
      arr[x][j]=0

for i in range(1, 4) :
  for j in range(1, 4) :
    print(arr[i][j], end=' ')
  print()
'''