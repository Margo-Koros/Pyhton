# 3.3[20]: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы и заранее известно какой алфавит надо использовать.

# Примеры/Тесты:
# Input:   ноутбук
# Output:  12

# Input:   notebook
# Output:  14

RU_Point1 = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
RU_Point2 = ['Д', 'К', 'Л', 'М', 'П', 'У']
RU_Point3 = ['Б', 'Г', 'Ё', 'Ь', 'Я']
RU_Point4 = ['Й', 'Ы']
RU_Point5 = ['Ж', 'З', 'Х', 'Ц', 'Ч']
RU_Point8 = ['Ш', 'Э', 'Ю']
RU_Point10 = ['Ф', 'Щ', 'Ъ']
ENG_Point1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
ENG_Point2 = ['D', 'G']
ENG_Point3 = ['B', 'C', 'M', 'P']
ENG_Point4 = ['F', 'H', 'V', 'W', 'Y']
ENG_Point5 = ['K']
ENG_Point8 = ['J', 'X']
ENG_Point10 = ['Q', 'Z']
Word = str(input ("Введите слово Word: "))
Word = Word.upper()
result = 0
for i in Word:
    if (i in RU_Point1):
        result = result + 1
    if (i in RU_Point2):
        result = result + 2
    if (i in RU_Point3):
        result = result + 3
    if (i in RU_Point4):
        result = result + 4
    if (i in RU_Point5):
        result = result + 5
    if (i in RU_Point8):
        result = result + 8
    if (i in RU_Point10):
        result = result + 10
    if (i in ENG_Point1):
        result = result + 1
    if (i in ENG_Point2):
        result = result + 2
    if (i in ENG_Point3):
        result = result + 3
    if (i in ENG_Point4):
        result = result + 4
    if (i in ENG_Point5):
        result = result + 5
    if (i in ENG_Point8):
        result = result + 8
    if (i in ENG_Point10):
        result = result + 10
print (result)