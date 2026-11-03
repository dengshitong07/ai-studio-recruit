T = int(input())
for _ in range(T):
    n = int(input())
    mid = n // 2
    for i in range(n):
        d = abs(i - mid)
        star = n - 2 * d
        # 关键修复：把 d 个空格拼在星号前面
        print(" " * d + "*" * star)