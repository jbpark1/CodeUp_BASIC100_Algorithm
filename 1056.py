a, b = map(int, input().split())

c = bool(a)
d = bool(b)

# 서로 다른 값일 때 True
# c=True / d=False -> True
# c=False / d=True -> True

# 같은 값일 때 False
# c=True / d=True -> False
# c=False / d=False -> False

print(c!=d)