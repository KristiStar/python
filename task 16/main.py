# # Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

#     5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input('Введите количество элементов в массиве: '))

x = int(input('Введите число: '))
import random
a = []
for i in range(n):
    arr = random.randint(1, 9) 
    a.append(arr) 

print(a)

count = 0 
for i in a:
    if i == x:
        count += 1

print(f'Введеное число {x} повторяется в массиве {count} раз') 