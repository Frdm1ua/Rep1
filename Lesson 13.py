def arithmetic(a, b, c):
    if c == '+':
        return(a + b)
    elif c == '-':
        return(a - b)
    elif c == '*':
        return(a * b)
    elif c == '/':
        return(a / b)
    else:
        return("Незвестная операция")


a = int(input('a: '))
b = int(input('b: '))
c = input('Действие(+, -, *, / ): ')

print(arithmetic(a, b, c))
