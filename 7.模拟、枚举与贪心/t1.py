n, t = map(int, input().split())
s = list(input().strip())

dot = -1

# 查找小数点
for k in range(len(s)):
    if s[k] == '.':
        dot = k
        break

# 没有小数点，直接输出
if dot == -1:
    print(''.join(s))
else:
    # 找到第一个大于等于 5 的小数位
    i = dot + 1
    while i < len(s) and s[i] < '5':
        i += 1

    # 不超过 t 次四舍五入
    while i < len(s) and t > 0:

        # 从目标数字的前一位开始进位
        p = i - 1

        # 跳过小数点
        if p == dot:
            p -= 1

        # 连续的 9 变成 0，继续向前进位
        while p >= 0 and s[p] == '9':
            s[p] = '0'
            p -= 1

            if p == dot:
                p -= 1

        t -= 1

        # 整数部分也全部是 9
        if p < 0:
            s = list('1' + '0' * dot)
            break

        # 正常进位
        s[p] = str(int(s[p]) + 1)

        # 进位到了整数部分
        if p < dot:
            s = s[:dot]
            break

        # 截掉已经舍弃的小数位
        s = s[:p + 1]

        # 如果进位后仍然 >= 5，可以继续四舍五入
        if s[p] >= '5':
            i = p
        else:
            break

    ans = ''.join(s)

    # 去掉小数末尾的 0
    if '.' in ans:
        ans = ans.rstrip('0').rstrip('.')

    print(ans)