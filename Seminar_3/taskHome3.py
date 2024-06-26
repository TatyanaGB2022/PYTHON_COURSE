# СКРАБЛ. В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# --------------------------------
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.
# Пример:
# k = 'ноутбук'
# # 12

k = 'ноутбук'
points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'} # словарь, 
# который связывает баллы соответствующих букв в английском алфавите 
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'} 
# словарь, который связывает баллы соответствующих букв в русском алфавите 
word = k.upper()  # Преобразуем все буквы в слове k в верхний регистр.
count = 0 # Инициализация переменной count, которая будет использоваться для подсчета общего количества баллов в слове.
for i in word: # Этот цикл проходит по каждой букве в слове
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM': # Это условие проверяет, является ли буква английской
        for j in points_en: # Если буква английская, этот цикл проходит по каждому ключу в словаре points_en
            if i in points_en[j]: # Если буква присутствует в значении текущего ключа, то…
                count = count + j # …к текущему значению count добавляется значение ключа
    else: # Если буква не английская, то…
        for j in points_ru: # …этот цикл проходит по каждому ключу в словаре points_ru.
            if i in points_ru[j]: # Если буква присутствует в значении текущего ключа, то…
                count = count + j # …к текущему значению count добавляется значение ключа.
print(count) # общее количество баллов выводится на экран.

'''
В общем, этот код подсчитывает количество баллов в слове для игры Scrabble, 
учитывая как английские, так и русские буквы. 
Баллы для каждой буквы определены в словарях points_en и points_ru. 
Код проходит по каждой букве в слове и добавляет соответствующее количество баллов к общему счету. 
Затем он выводит общий счет.
'''

# 2 вариант
dict_1 = {1:'AEIOULNSTRАВЕИНОРСТ',
2:'DGДКЛМПУ',
3:'BCMPБГЁЬЯ',
4:'FHVWYЙЫ',
5:'KЖЗХЦЧ',
8:'JXШЭЮ',
10:'QZФЩЪ'}
k = 'ноутбук'
count = 0

for l in k.upper():
    for i, j in dict_1.items() :
        if l in j:
            count += i
print(count)