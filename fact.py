# Найти факториал заданного числа, через рекурсию

def fact(n):
    if n <=1:
        return n
    else:
        return n * fact(n-1)
print(fact(int(input('введите число: '))))
        