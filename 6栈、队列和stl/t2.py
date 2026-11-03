n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = sum(b)

diff = []
for i in range(n):
    diff.append(a[i] - b[i])

diff.sort(reverse=True)

for i in range(k):
    ans += diff[i]

print(ans)