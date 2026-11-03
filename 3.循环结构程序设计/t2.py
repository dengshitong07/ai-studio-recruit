n = int(input())
num = 1
for i in range(1, n + 1):
    line = []
    for _ in range(i):
        line.append(f"{num:4d}")
        num += 1
    print("".join(line))