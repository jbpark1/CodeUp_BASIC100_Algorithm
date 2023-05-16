n = int(input())
a = input().split()

for i in range(n):          #0부터 n-1까지
    a[i] = int(a[i])        #a에 순서대로 저장

d = []                      #어떤 데이터 목록을 순서대로 저장하기 위해 아무것도 없는 리스트 변수 만들기
for i in range(24):
    d.append(0)             #[0,0,0, ..., 0]과 같이 24개의 정수 값 0을 추가해넣음

for i in range(n):
    d[a[i]]+=1

for i in range(1,24):
    print(d[i], end=' ')