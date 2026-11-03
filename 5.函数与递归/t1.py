def count_two(x):
    ans = 0
    i = 1

    while i <= x:
        high = x // (i * 10)
        cur = (x // i) % 10
        low = x % i

        if cur < 2:
            ans += high * i
        elif cur == 2:
            ans += high * i + low + 1
        else:
            ans += (high + 1) * i

        i *= 10

    return ans


L, R = map(int, input().split())

print(count_two(R) - count_two(L - 1))