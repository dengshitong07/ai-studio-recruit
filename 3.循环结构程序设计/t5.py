while True:
    try:
        n = int(input())
        # 上半段：i 从 0 ~ n
        for i in range(n + 1):
            print("  " * (n - i) + "*" * (i + 1))
        # 下半段：i 从 0 ~ n-1
        for i in range(n):
            print("  " * (i + 1) + "*" * (n - i))
    except EOFError:
        break