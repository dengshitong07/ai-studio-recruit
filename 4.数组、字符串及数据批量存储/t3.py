n, k, m = map(int, input().split())
people = list(range(n))
pos = k
while len(people) > 1:
    pos = (pos + m - 1) % len(people)
    people.pop(pos)
print(people[0])