import sys
from math import gcd

# 九宫格每个数字对应的坐标
pos = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '7': (2, 0), '8': (2, 1), '9': (2, 2)
}

def check(s):
    used = set()

    for i in range(len(s)):
        x = s[i]

        # 数字不能重复
        if x in used:
            return False

        # 检查当前数字与上一个数字之间的连线
        if i > 0:
            last = s[i - 1]

            x1, y1 = pos[last]
            x2, y2 = pos[x]

            dx = x2 - x1
            dy = y2 - y1

            g = gcd(abs(dx), abs(dy))

            # 检查线段经过的所有中间数字
            for k in range(1, g):
                mx = x1 + dx * k // g
                my = y1 + dy * k // g

                middle = str(mx * 3 + my + 1)

                if middle not in used:
                    return False

        used.add(x)

    return True


# 多行输入，读取到文件结束
for s in sys.stdin:
    s = s.strip()

    if s:
        print("YES" if check(s) else "NO")