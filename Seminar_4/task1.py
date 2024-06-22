# Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
'''''
# st = "8 7 6 + j m + 0"
# st = st.replace(" ", "").split('+')
# print(st)
'''
# 1 вариант
# input_string = "a a a b c a a d c d d"
# characters = input_string.split()
# occurrences = {}
# result = []
# for i in characters:
#   if i in occurrences:
#     occurrences[i] += 1
#     result.append(f"{i}_{occurrences[i]}")
#   else:
#     occurrences[i] = 0
#     result.append(i)
# print(*result)

# 2 вариант
# list_letter = 'a a a b c a a d c d d'.split()
# letter_new = []
# letter_dict = {}
# for letter in list_letter:
#   if letter in letter_dict.keys():
#     letter_dict[letter] += 1
#     letter_new.append(f'{letter}_{letter_dict[letter]}')
#   else:
#     letter_dict[letter] = 0
#     letter_new.append(letter)
# print(*letter_new)

# #3 вариант
# dict = {} #объявляем словарь
# string = "a a a b c a a d c d d"
# string_res = ""

# for i in string.split(): #проходимся по строке с разделителем. i перебирает буквы поочереди, split()убирает 
#   # пробелы
#   count = dict.get(i) #
#   if count != None:
#     string_res = string_res + i + "_" + str(count) + " "#ищем есть ли буква в словаре, если ее нет, то добавляем
#     dict[i] = count + 1
#   else:
#     dict[i] = 1
#     string_res = string_res + i + " "#выводим букву в результирующую строку

# print(string_res)

#4 вариант лучший
dict = {} #объявляем словарь
string = "a a a b c a a d c d d"
string_res = ""

for i in string.split(): #проходимся по строке с разделителем. i перебирает буквы поочереди, split()убирает 
  # пробелы
  if i in dict: # i это первая буква (а). есть ли у нас ключ с а? если есть
    string_res = string_res + i + "_" + str(dict[i]) + " " #ищем есть ли буква в словаре, если ее нет, то добавляем
  else: #если в 62 строке false. если этого ключа нет в словаре
    string_res = string_res + i + " " #выводим букву в результирующую строку
  dict[i] = 1 + dict.get(i, 0) #если есть ключ, то выдает значение ключа, а если его нет, то выдает значение 0, 
  # то есть, если нет ключа то dict[i] = 1 + dict.get(i, 0) принимает значение dict[i] = 1 (создаем ключ а со 
  # значением 1), если есть ключ, то dict[i] = 1 + dict.get(i, 0) принимает dict[i] = dict[i] + 1 (значение ключа а 
  # увеличивается на одно.)
print(string_res)