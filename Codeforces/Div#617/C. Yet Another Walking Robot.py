def int_input():
    return int(input())


def str_input():
    return input()


directions = {
    "L": -1,
    "R": 1,
    "U": 1,
    "D": -1
}

t = int_input()

for i in range(t):
    n = int_input()
    x, y = 0, 0
    s = str_input()
    travel_dict = {(0, 0): 0}
    travel_list = [(x, y)]
    for j in range(n):
        if s[j] == "L" or s[j] == "R":
            x += directions.get(s[j])
            travel_list.append((x, y))

        else:
            y += directions.get(s[j])
            travel_list.append((x, y))

        if (x, y) not in travel_dict.keys():
            travel_dict[(x, y)] = j + 1
        else:
            print(travel_dict[(x, y)] + 1, j + 1)
            break
        if j+1 == n:
            print(-1)
