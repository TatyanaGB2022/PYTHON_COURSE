# Задача №3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

a = int(input("Вевдите количество учеников в первом классе: "))
b = int(input("Вевдите количество учеников во втором классе: "))
c = int(input("Вевдите количество учеников в третьем классе: "))

# s1 = (a//2 + a%2) остаток от деления для того, если количество учеников нечетное, например 11
# s2 = (b//2 + b%2)
# s3 = (c//2 + c%2)

# print(s1 + s2 + s3)

# второе решение работает только для двойки. Если человек за партой, например 5, то не подходит решение
# s1 = ((a + 1)//2)
# s2 = ((b + 1)//2)
# s3 = ((c + 1)//2)
# print(s1 + s2 + s3)

#третье решение
# s1 = (a // 2) + (a%2!=0) # если a%2!=0 a%2 не равно 0, то будет 1 (true, false)
# s2 = (b // 2) + (b%2!=0) 
# s3 = (c // 2) + (c%2!=0) 
# print(s1 + s2 + s3)

s1 = abs (-a // 2)  #abs absolute
s2 = abs (-b // 2)
s3 = abs (-c // 2)
print(s1 + s2 + s3)