# Example 2-5. Initializing a tuple and an array from a generator expression

symbols = '$¢£¥€¤'
codes = tuple(ord(symbol) for symbol in symbols)
print(codes)

codes_v2 = tuple([ord(symbol) for symbol in symbols])
print(codes_v2)