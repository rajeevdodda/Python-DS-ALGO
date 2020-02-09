def total(s):
    q = s // 10
    r = s % 10
    if q == 0:
        return r
    return q * 10 + total(q + r)


t = int(input())

for i in range(t):
    s = int(input())
    print(total(s))
