while True:
    i = input()

    if i == "0 0":
        break

    print(sum(map(int, i.split())))
