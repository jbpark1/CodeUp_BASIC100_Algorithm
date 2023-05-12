n = int(input())

# 9 -> 1 2 X 4 5 X 7 8 X
# 29 -> 1 2 X 4 5 X 7 8 X 10 11 12 X 14 15 X
# 10으로 나눴을 때 3의 배수인 것

for i in range(1, n+1):
    if(i%10==3):
        print("X", end=' ')
    elif(i%10==6):
        print("X", end=' ')
    elif(i%10==9):
        print("X", end=' ')
    else:
        print(i, end=' ')