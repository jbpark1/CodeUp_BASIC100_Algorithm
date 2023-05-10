n = int(input())

# // 연산자: 정수 몫

if(n//3==1):            #3, 4, 5
    print("spring")
elif(n//3==2):          #6, 7, 8
    print("summer")
elif(n//3==3):          #9, 10, 11
    print("fall")
else:                   #12, 1, 2
    print("winter")