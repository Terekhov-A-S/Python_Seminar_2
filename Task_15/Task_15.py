# Задача 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

def Check_factorial (num):
    count = 1
    for i in range(1, num + 1):
        count *= i
    return count
j = int (input ('Введите число: '))
print (f'Полученный набор призведений от 1 до {j} : ', end = '')
for i in range(1, j + 1):
    if i == j: 
        print (f'{Check_factorial(i)}')
    else:
        print (f'{Check_factorial(i)}', end = ', ')