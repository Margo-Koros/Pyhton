# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

import random as r
def powerOfNumber(A, B):
    if (B==0):
        return 1
    else:
        return A*powerOfNumber(A,B-1)

a = int(input('Введите число A: '))
print()
b = int(input('Введите степень B: '))
print()
print (powerOfNumber(a,b))