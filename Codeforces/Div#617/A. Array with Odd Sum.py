t = int(input())
for i in range(t):
    n = int(input())
    arr = list(int(i) for i in input().split())
    if sum(arr) % 2 == 0:
        print("NO")
    else:
        print("YES")
