H, M = map(int, input().split())

m = H * 60 + M - 45

if m >= 0:
    print(m // 60, m % 60)
else:
    print(23, 60 + m)
