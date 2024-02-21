word = input().upper()
c = []

for i in range(65, 91):
    c.append(word.count(chr(i)))

if c.count(max(c)) > 1:
    print("?")
else:
    print(chr(c.index(max(c)) + 65))
