# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def recursive_power(a, b):
   
    if b == 0:
        return 1

    elif b == 1:
        return a
   
    else:
        return a * recursive_power(a, b-1)


a = int(input('Введите число a: '))

b = int(input('Введите степень b: '))


result = recursive_power(a, b)
print(result)