import sys

K, N = map(int, input().split())

lan = [int(sys.stdin.readline()) for i in range(K)]
start = 1
end = max(lan)

while start <= end:
    total = 0
    length = (start + end) // 2

    for j in lan:
        total += j // length

    if total >= N:
        start = length + 1
    else:
        end = length - 1

print(end)
