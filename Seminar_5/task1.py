# Задача №31. факториал числа n через рекурсию
# 1 вариант
# def fact(n):
#   if n == 1:
#     return 1
#   return n * fact(n - 1)

# a = fact(5)
# print(a)

# 2 вариант
# def fac(n):
#   if n == 1:
#     return 1
#   return fac(n - 1) * n

# print(fac(int(input())))

# 3 вариант
def fact(n):
  if n < 0:
    return "Ошибка ввода"
  if n == 0:
    return 1
  return n * fact(n-1)

print(fact(6))