# Определить полиндром введеное слово или нет через рекурсию

def revs1(n):
  if n[0] != n[-1]:  #n[0] первая буква в слове, n[-1] - последняя буква
    return False  #если False, то слово не полиндром
  elif len(n) <= 1:
    return True
  return revs1(n[1:-1]) #делаем срез и убираем первую и последнюю букву. -1 потому что не захватывает последнюю
print(revs1("казак")) # True полиндром
