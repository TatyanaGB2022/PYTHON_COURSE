# Задача N35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n (само число)
# Input: 5 
# Output: yes

def Simple (Turn, del1 = 2):
  if del1 * del1 >= Turn:
    return True
  elif Turn % del1 == 0:
    return False
  else:
    return Simple(Turn, del1 + 1)
Simple(10)
