s = input().strip()

count = 0
good = True

for c in s:
    if c == 'a':
        count += 1
    else:
        count -= 1

    if count < 0:
        good = False
        break

if count != 0:
    good = False

if good:
    print("Good")
else:
    print("Bad")