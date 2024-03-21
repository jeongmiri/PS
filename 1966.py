T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))
    queue = [(i, imp[i]) for i in range(len(imp))]
    imp.sort(reverse=True)
    k = 0

    for j in imp:
        while queue[0][1] != j:
            tmp = queue.pop(0)
            queue.append(tmp)

        k += 1

        if queue.pop(0)[0] == M:
            break

    print(k)
