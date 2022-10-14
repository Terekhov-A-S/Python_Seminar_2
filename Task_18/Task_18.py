# 18). Реализуйте алгоритм перемешивания списка.

from random import randint
 
list = [1, 4, 5, 6, 3]
print ("Оригинальный список: " + str(list))
for i in range(len(list)-1, 0, -1):
    j = randint(0, i + 1)
    list[i], list[j] = list[j], list[i]
print ("Список после перемешивания: " +  str(list))