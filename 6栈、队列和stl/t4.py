from functools import cmp_to_key

n = int(input())
a = input().split()

def cmp(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

a.sort(key=cmp_to_key(cmp))

print(''.join(a))