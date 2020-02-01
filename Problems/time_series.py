stock_prices = [6, 4, 1, 2, 1, 3, 5]
span = [1]
# O(N^2)
for i in range(1, len(stock_prices)):
    count = 0
    for j in range(i, -1, -1):
        if stock_prices[j] <= stock_prices[i]:
            count += 1
        else:
            break
    span.append(count)

# O(N)
stack = [0]
span = [1]
for i in range(1, len(stock_prices)):



    pass
