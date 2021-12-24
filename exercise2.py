from functools import reduce

people = [{'name': 'Maria', 'height': 160},
          {'name': 'João', 'height': 80},
          {'name': 'Joana'}]

height_count = reduce(lambda a, x: a + 1, filter(lambda x: 'height' in x, people), 0)
print(height_count)

height_total = reduce(lambda a, x: a + x['height'], filter(lambda x: 'height' in x, people), 0)
print(height_total)
print(height_total / height_count)
