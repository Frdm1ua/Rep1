import random
from collections import Counter
a = [random.randint(0,7) for i in list(range(10))]
b = [random.randint(0,7) for i in list(range(10))]
print(a)
print(b)
print("Уникальные числа списков a и b:", len(Counter(a+b).keys()))

