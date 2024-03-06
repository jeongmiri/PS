import sys


n = int(input())
temp = [int(sys.stdin.readline()) for i in range(n)]
stack = []
op = []
cur = 1

for i in temp:
    while cur <= i:
        op.append('+')
        stack.append(cur)
        cur += 1

    if stack.pop() != i:
        print("NO")
        sys.exit()

    op.append('-')

print('\n'.join(op))
