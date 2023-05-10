a = int(input())        #55
b = 0                   #1부터 키워가는 수
s = 0                   #합계

while True:
    b+=1
    s+=b
    if s>=a:
        print(b)
        break