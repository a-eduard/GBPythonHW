# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3), 100 -> 1 (1 + 0 + 0)

x = int(input('Введите число: '))

a = x // 100
b = (x //10) % 10
c = x % 10

print(a+b+c)