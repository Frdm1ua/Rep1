import random
height = int(input("Введите рост Пети: "))
a = [random.randint(150, 200) for i in list(range(10))]
a.sort(reverse=True)
print(a)
point = 0
while point < len(a) and a[point] >= height:
    point += 1
print("Место в строю:", point + 1)