#ord(): 알파벳의 정수값
c = ord(input())
t = ord('a')

while(t<=c):
    print(chr(t), end=" ")
    t=t+1