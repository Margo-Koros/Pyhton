# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

import random as r
def sum(A, B):
    if (B==0):
        return A
    else:
        return sum(A+1,B-1)

a = int(input('Введите число A: '))
print()
b = int(input('Введите число B: '))
print()
if (a>=b):
    print (sum(a,b))
else:
    print(sum(b,a))