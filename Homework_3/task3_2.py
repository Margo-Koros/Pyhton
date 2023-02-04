# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

import random as rn

N = int(input ("input N: "))
X = int(input ("input X: "))
result = N
l=[]
for i in range (0,N):
    l.append(rn.randint(0,N))
print(X)
print(l)
delta = abs(l[i]-X)
for i in range(len(l)):
    if (delta == abs(l[i]-X)):
        if l[i] < result:
            result = l[i]
    if delta > abs(l[i]-X):
        delta = abs(l[i]-X)
        result = l[i]
print(result)