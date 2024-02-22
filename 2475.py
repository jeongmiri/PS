n = map(int, input().split())
s = [i ** 2 for i in n]

print(sum(s) % 10)
