def lcm_v1(x, y):
    greater = max(x, y)

    while True:

        if greater % x == 0 and greater % y == 0:
            return greater
        else:
            greater += 1


def gcd(x, y):
    while y:
        x, y = y, x % y

    return x


def lcm_v2(x, y):
    return (x * y) // gcd(x, y)


print(lcm_v1(54, 24))

print(gcd(54, 24))
print(gcd(24, 54))
