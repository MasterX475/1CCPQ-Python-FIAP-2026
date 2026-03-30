import math
import random

num = 17
raiz = math.sqrt(num)
print(f"A raiz do {num} é {raiz:.2f}")

graus = 45
radiano = graus / 180 * math.pi
seno = math.sin(radiano)
print (f"O seno é {seno:.2f}")

num_random = random.random()
print(num_random)

num_random_int = random.randint(1, 10)
print(num_random_int)