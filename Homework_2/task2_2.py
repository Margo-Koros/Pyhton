# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3
# Примечание.
# Здесь нужно составить два уравнения. Которые приведут к квадратному уравнению.
# Кто не помнит, как решать квадратное уравнение - посмотрите в сети. Обойдите дополнительной проверкой возможность комплексных решений. 
# Можно игнорировать то, что получаться рациональные решения вместо натуральных.

# Для вычисления квадратного корня используйте возведение в степень 0.5 

def fXY(s,p):
    a = []
    D = s**2-4*p
    if D<0:
        print("не могу решить")
    elif D == 0:
        a.append(s/2)
        a.append(s/2)
    else:
        a.append((s+D**0.5)/2)
        a.append((s-D**0.5)/2)
    return a
import random as r
x = r.randint(0,1000)
y = r.randint(0,1000)
print ('Загаданные числа:', x, y)
s = x+y
p = x*y
print ('Сумма чисел:', s, 'их произведение:', p)
a = fXY(s,p)
print("ответ: ", a)