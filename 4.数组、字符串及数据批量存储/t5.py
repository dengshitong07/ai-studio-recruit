# 月亮 30 天一个周期
cycle = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
         14,13,12,11,10,9,8,7,6,5,4,3,2,1]

n = int(input())
a = list(map(int, input().split()))

# 枚举：找所有可能的起始偏移
candidates = []
L = len(cycle)
for start in range(L):
    ok = True
    for i in range(n):
        if cycle[(start + i) % L] != a[i]:
            ok = False
            break
    if ok:
        # 最后一天在周期里的位置：start + n - 1
        pos = (start + n - 1) % L
        next_val = cycle[(pos + 1) % L]
        candidates.append(next_val)

# 如果所有候选的 next_val 一样，就能判断；否则 -1
if all(x == candidates[0] for x in candidates):
    last = a[-1]
    nv = candidates[0]
    if nv > last:
        print("UP")
    else:
        print("DOWN")
else:
    print("-1")