# Example 3-7. StrKeyDict0 converts nonstring keys to str on lookup
class StrKeyDict0(dict):
    def __missing__(self, key):
        print("missing")
        print(type(self), self)
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        print("get")
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d.get(2))

print(2 in d)
