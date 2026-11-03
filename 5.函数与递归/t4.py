x, y = map(int, input().split())

ans = 0

for i in range(x, y + 1):
    s = sum(map(int, str(i)))

    if s % 5 == 0:
        ans += 1

print(ans)