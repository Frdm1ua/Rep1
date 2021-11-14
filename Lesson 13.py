def arithmetic(a, b, c):
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '*':
        print(a * b)
    elif c == '/':
        print(a / b)
    else:
        return ("Незвестная операция")


a = int(input('a: '))
b = int(input('b: '))
c = input('Действие(+, -, *, / ): ')

arithmetic(a, b, c)
