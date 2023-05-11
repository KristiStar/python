# Напишите рекурсивную функцию sum(a, b), возвращающую 
# сумму двух целых неотрицательных чисел. Из всех арифметических 
# операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*

# 2 2
#     4

def sum(a, b):

    if b == 0:
        return a

    elif b > 0:
        return sum(a+1, b-1)

    else:
        return sum(a-1, b+1)


a = int(input('Введите число а: '))

b = int(input('Введите число b: '))


result = sum(a, b)

print(result)