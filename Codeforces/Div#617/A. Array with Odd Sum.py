t = int(input())
for i in range(t):
    n = int(input())
    arr = list(int(i) for i in input().split())
    even = 0
    for j in arr:
        if j % 2 == 0:
            even += 1

    if n %2 == 0:
        if n == even or even == 0:
            print("NO")
        else:
            print("YES")
    else:
        if n == even:
            print("NO")
        else:
            print("YES")

