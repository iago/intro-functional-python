from functools import reduce
import random

names = ['Maria', 'João', 'Joana']
name_lengths = map(len, names)
print(list(name_lengths))

squares = map(lambda x: x * x, range(5))
print(list(squares))

codenames = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
secret_names = map(lambda x: random.choice(codenames), names)
print(list(secret_names))

hash_names = map(lambda x: hash(x), names)
print(list(hash_names))

sentences = ['Joana lê livros',
             'João viu Joana',
             'Joana tropeçou']

joana_count = reduce(lambda a, x: a + x.count('Joana'), sentences, 0)
print(f'joana_count = {joana_count}')

