# Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму

num = int (input ("Введите число: "))
list = [round ((1 + 1 / n) ** n, 3) for n in range (1, num + 1)]
print (f"Последовательность: {list}")
print (f"Сумма: {round (sum (list), 3)}")
