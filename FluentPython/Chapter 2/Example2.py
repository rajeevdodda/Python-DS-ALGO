# Example 2-2. Build a list of Unicode codepoints from a string, take two

symbols = '$¢£¥€¤'

codes = [ord(symbol) for symbol in symbols]
print(codes)

x = 'ABC'
dummy = [x for x in x]
print(dummy)
print(x)
