# Задача №45. Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все
# пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 300
# Вывод: 220 284
'''''
Дружественные числа это пара различных натуральных числа, для которых сумма всех собственных делителей первого 
числа равна второму числу и наоборот.

Например: Делители числа 220: 1;2;4;5;10;11;20;22;44;55;110. 
          Делители числа 284: 1;2;4;71;142
Если просуммируем все делители первого числа, то получится 1+2+4+5+10+11+20+22+44+55+110=284.
А теперь просуммируем делители числа 284: 1+2+4+71+142 = 220 – так и выглядит в математике эффект
дружественных чисел.
'''''

# 1 вариант
# k = 300
# a = []
# b = []
# for i in range(k):
#   summa = 0
#   for j in range(1, i // 2 + 1):  
#     if i%j==0:
#       summa += j
#   if summa > 1:
#     a.append(summa)
#     b.append(i)
# # print(summa)
# # print(a)
# # print(b)

# for z in range(len(a)):
#   for y in range(z):
#     if a[z] == b[y] and b[z] == a[y]:
#       print(b[z], b[y])

# 2 вариант - лучше. Через кортеж
n = int(input())
list_1 = list()
for i in range(n):
  summa = 0
  for j in range(1, i // 2 + 1):
    if i % j == 0:
      summa += j
      list_1.append(tuple([i, summa]))        

for i in range(len(list_1)):
  for j in range(i, len(list_1)):
    if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] == list_1[j][0]:
      print(*list_1[i])
