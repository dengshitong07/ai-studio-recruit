a = list(map(int, input().split()))

# 统计奇数次出现的数字
odd = []
for i in range(10):
    if a[i] % 2 == 1:
        odd.append(i)

# 超过一个奇数，无法组成回文数
if len(odd) > 1:
    print(-1)

else:
    # 每个数字可以组成多少对
    half = []
    for i in range(10):
        half.extend([str(i)] * (a[i] // 2))

    # 没有任何数字可以组成一对
    if len(half) == 0:
        if len(odd) == 1:
            print(odd[0])
        else:
            print(-1)

    else:
        # 找到最小的非零数字，避免前导 0
        first = -1

        for i in range(len(half)):
            if half[i] != '0':
                first = i
                break

        # 没有非零数字可以放在第一位
        if first == -1:
            print(-1)

        else:
            # 把最小的非零数字放到第一位
            half[0], half[first] = half[first], half[0]

            # 中间的数字
            middle = str(odd[0]) if odd else ''

            # 组成最小回文数
            left = ''.join(half)
            ans = left + middle + left[::-1]

            print(ans)