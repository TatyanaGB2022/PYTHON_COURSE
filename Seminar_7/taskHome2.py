# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках 
# не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза 
# может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод: Парам пам-пам

stroka = "пара-ра-рам рам-пам-папам па-ра-па-дам"

vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = stroka.split()
if len(phrases) < 2:
  print('Количество фраз должно быть больше одной!')
else:
  countVowels = []

  for i in phrases:
    countVowels.append(len([x for x in i if x.lower() in vowels]))

  if countVowels.count(countVowels[0]) == len(countVowels):
    print('Парам пам-пам')
  else:
    print('Пам парам')


# def count_vowels(word):
#     vowels = "аеёиоуыэюя"
#     return sum(1 for char in word if char in vowels) 

# def check_rhythm(stroka):
#     phrases = stroka.split()
    
#     if len(phrases) < 2:
#         return "Количество фраз должно быть больше одной!"
    
#     syllables_count = [sum(count_vowels(word) for word in phrase.split('-')) for phrase in phrases]
    
#     if all(count == syllables_count[0] for count in syllables_count):
#         return "Парам пам-пам"
#     else:
#         return "Пам парам"
# print(check_rhythm(stroka))