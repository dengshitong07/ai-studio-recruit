ch = input().strip()
end = ord(ch) - ord('A')
for i in range(end + 1):
    # 前面空格
    print(" " * (end - i), end="")
    # 上升部分
    for j in range(i + 1):
        print(chr(ord('A') + j), end="")
    # 下降部分
    for j in range(i - 1, -1, -1):
        print(chr(ord('A') + j), end="")
    print()