#입력 받음
arr = []
for i in range(10):
    temp = list(map(int, input().split()))
    arr.append(temp)

#입력 -> 오류코드
# for i in range(10):
#     a = input().split()
#     for j in range(10):
#         arr[i][j] = a[j]

arr[1][1]=9     #(2,2)지점에서 출발

#개미굴 탐색
for i in range(10):
    for j in range(10):
        if arr[i][j]==1:    #장애물
            arr[i][j]=1
        elif arr[i][j]==9 and arr[i][j+1]==0:   #우측 이동
            arr[i][j+1]=9
        elif arr[i][j]==9 and arr[i][j+1]==1 and arr[i+1][j]==0:    #하단 이동
            arr[i+1][j]=9
            
        # if arr[i+1][j+1]==1:
        #     arr[i+1][j+1]=1
        # elif arr[i+1][j+1]==9 and arr[i+1][j+2]==0:
        #     arr[i+1][j+2]=9
        # elif arr[i+1][j+1]==9 and arr[i+1][j+2]==1 and arr[i+2][j+1]==0:
        #     arr[i+2][j+1]=9

for i in range(10):
    for j in range(10):
        # if arr[i][j]==9 and arr[i][j+1]==2:
        #     arr[i][j+1]=9
        # elif arr[i][j]==9 and arr[i+1][j]==2:
        #     arr[i+1][j]=9
            
        if arr[i][j]==9 and arr[i][j+1]==2:     #우측에서 먹이 발견
            arr[i][j+1]=9
        elif arr[i][j]==9 and arr[i][j+1]==1 and arr[i+1][j]==2:   #하단에서 먹이 발견
            arr[i+1][j]=9

#출력
for i in range(10):
    for j in range(10):
        print(arr[i][j], end=' ')
    print()