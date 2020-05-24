# Example 2-3. The same list built by a listcomp and a map/filter composition

symbols = '$¢£¥€¤'

beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print(beyond_ascii)

beyond_ascii_v2 = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii_v2)