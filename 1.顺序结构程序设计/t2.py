def check(num1, num2, num3):
    s = str(num1) + str(num2) + str(num3)
    if len(s) != 9:
        return False
    return set(s) == {'1','2','3','4','5','6','7','8','9'}

res = []
# 两种合法情况：一位数 × 四位数；两位数 × 三位数
# 情况 1：1位 * 4位
for a in range(1, 10):
    for b in range(1000, 9999):
        c = a * b
        if check(a, b, c):
            res.append((c, a, b))
# 情况 2：2位 * 3位
for a in range(10, 99):
    for b in range(100, 999):
        c = a * b
        if check(a, b, c):
            res.append((c, a, b))

# 排序：先按结果，再按小乘数
res.sort(key = lambda x: (x[0], x[1]))
for c, a, b in res:
    print(f"{c} = {a} x {b}")