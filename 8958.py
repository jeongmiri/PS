import sys

n = int(input())

for _ in range(n):
    score = 0
    result = sys.stdin.readline().strip()

    for i in result.split("X"):
        score += ((len(i) * (len(i) + 1)) // 2)

    print(score)
