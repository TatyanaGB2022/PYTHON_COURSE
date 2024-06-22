# def f(x):
# return x

# print(f(5))

# f1 = lambda x: x
# print(f1(5))
# print((lambda x:x)(5))

# ВСЕ по функции map
num = '2 4 7 4 1'.split()
# num = num.split() # ОШИБКА !!!!!
print(num)
num1 = list(map(int,num))
print(num1)

num1 = list(map(lambda x:int(x),num))
print(num1)

num1 = list(map(lambda x: x*2,num1))
print(num1)

# ////////////////////ВСЕ по функции filter/////////////////////

num1 = list(filter(int,num1))
print(num1)
