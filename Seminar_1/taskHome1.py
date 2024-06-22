# Задача 2: Найдите сумму цифр трехзначного числа. 
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# 1 вариант
# n = int (input("Введите трехзначное число: "))
# res = 0
# while n > 0:
#   print(n)
#   res += n % 10
#   n //=10
# print(res)

# 2 вариант
# number = int(input("Введите трехзначное число: "))
# res = number % 10 + (number // 10 % 10) + (number // 100)

# print(res)

# 3 вариант
m = int(input())
sum = 0
for i in range(len(str(m))):
  sum += m // 10 ** i % 10
print(sum)




