# 17). Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) 
# в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2


from random import randint

with open ('file.txt', 'w') as data:
    data.write ('0\n')
    data.write ('1\n')
    data.write ('5\n')
    data.write ('8\n')
    data.write ('10\n')

def numbers (n):
    return [randint (-n/2, n) for i in range (-n, n + 1)]

def list_in_file (path):
    data = open (path, 'r')
    dlist = [int (line.strip()) for line in data]
    data.close ()
    return dlist

def get_mult (numbers, datalist):
    mult = 1
    for i in datalist:
        mult *= numbers [i]
    return mult

path = 'file.txt'
n = 10 
datalist = list_in_file (path)
numbers = numbers (n)

print (numbers)
print (datalist)
print (get_mult (numbers, datalist))