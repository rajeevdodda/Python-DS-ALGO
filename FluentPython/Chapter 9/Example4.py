# Example 9-4. Comparing behaviors of classmethod and staticmethod


class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


print(Demo.klassmeth())
print(Demo.klassmeth("spam"))

print(Demo.statmeth())
print(Demo.statmeth("spam"))

