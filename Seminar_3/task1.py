# Задача №17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения списка или список задан изначально.

# 1 вариант
# lists = [1, 1, 2, 0, -1, 3, 4, 4]
# unique_numbers = set(lists)  
# count = len(unique_numbers)  
# print(count)
# # Преобразуем список в множество и подсчитываем количество элементов в множестве

# # 2 вариант
# Input = [1, 1, 2, 0, -1, 3, 4, 4]
# Output = []
# for i in Input:
#   if i not in Output:
#     Output.append (i)
# print(Input, "\n")
# print ("Уникальных значений: ",len(Output), "\n")

#3 вариант
sp = [1, 1, 2, 0, -1, 3, 4, 4]
a = list()
for c in sp:
  if c not in a:
    a.append(c)
print(len(a))