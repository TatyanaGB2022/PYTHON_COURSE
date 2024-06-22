# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, спов торениями). Выдать без повторений 
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# 1 вариант
# var1 = '5 4'
# var2 = '1 3 5 7 9'
# var3 = '2 3 4 5'

# var2 = set(var2.split()) #split преобразует строку в список
# print(var2)

# var3 = set(var3.split()) #set превращает в множество и удаляем повтор
# print(var3)

# i = var2.intersection(var3) # intersection ищет пересечения

# res = list(tuple(i))

# for i in range(len(res)):
#    for j in range(len(res) - i - 1):
#       if res[j] > res[j + 1]:
#          res[j], res[j + 1] = res[j + 1], res[j]

# print(*res)


# 2 вариант
var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел

var1 = var1.split() #split преобразует строку в список
var2 = var2.split()
var3 = var3.split()
set2 = set(var2) #set превращает в множество и удаляем повтор
set3 = set(var3)
var4 = set2.intersection(set3) # intersection ищет пересечения
print(*sorted(var4)) # *sorted возвращает новый отсортированный список

# 3 вариант
# var1 = '5 4' 
# var2 = '1 3 5 7 9' 
# var3 = '2 3 4 5' 
# mol = [int(x) for x in var1.split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#    set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#    print(i, end=' ')
