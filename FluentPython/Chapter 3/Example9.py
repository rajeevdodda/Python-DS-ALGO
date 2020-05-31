# Example 3-9. MappingProxyType builds a read-only mappingproxy instance from a dict

from types import MappingProxyType


d = {1: 'A'}
d_proxy = MappingProxyType(d)

print(type(MappingProxyType))
print(type(d_proxy))
print(d_proxy)

print(d_proxy[1])
try:
    d_proxy[2] = "B"
except TypeError as e:
    print(e)

d[2] = "B"
