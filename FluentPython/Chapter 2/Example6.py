# Example 2-6. Cartesian product in a generator expression

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
t_shirts_genexp = ((color, size) for color in colors for size in sizes)

for t_shirt in t_shirts_genexp:
    print(*t_shirt)