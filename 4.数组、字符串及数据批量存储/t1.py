import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    T = data[idx]
    idx += 1
    for _ in range(T):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        ma = max(a)
        mi = min(a)
        mean = sum(a) / n
        va = sum((x - mean) ** 2 for x in a) / n
        print("%d %.3f" % (ma - mi, va))

if __name__ == "__main__":
    main()