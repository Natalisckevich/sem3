# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число: '))
print(bin(num))

binary_num = ''

while num > 0:
    binary_num += str(num % 2)
num = num // 2
print(binary_num)

