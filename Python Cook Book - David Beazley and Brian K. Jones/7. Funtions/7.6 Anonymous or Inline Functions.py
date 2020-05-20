add = lambda x, y: x + y
print(help(add))

print(add(1, 3))
print(add("hello ", "world"))

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
names.sort(key=lambda name: name.split()[-1].lower())
print(names)
