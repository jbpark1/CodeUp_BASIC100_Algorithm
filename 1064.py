a, b, c = map(int, input().split())

#d = (a if (a<b) else b)    #a, b 중 작은거 = d
#e = (c if (c<d) else d)    #d, c 중 작은거 = e
#print(e)

print(a if (a<b) else b if (a if (a<b) else b)<c else c)