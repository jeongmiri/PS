import sys

n = [int(sys.stdin.readline()) for i in range(10)]
r = [i % 42 for i in n]

print(len(set(r)))
