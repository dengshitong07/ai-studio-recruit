n, x = map(int, input().split())
cnt = 0
for num in range(1, n + 1):
    t = num
    while t > 0:
        if t % 10 == x:
            cnt += 1
        t = t // 10
print(cnt)