def productdigits(с):
    a = 1
    for i in с:
        if int(i) != 0:
            a *= int(i)
    return a


x = input('Дано число:')
print("Результат:", productdigits(x))