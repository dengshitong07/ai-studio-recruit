import sys
import calendar

for line in sys.stdin:
    y, m, x = map(int, line.split())

    days = calendar.monthrange(y, m)[1]

    ans = 0

    for d in range(1, days + 1):
        date = f"{y:04d}-{m:02d}-{d:02d}"
        ans += date.count(str(x))

    print(ans)