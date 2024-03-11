#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код
first = my_favorite_movies[:10]
print(first)

last_ind = my_favorite_movies.rindex(',')#ищем последнюю запятую
last = my_favorite_movies[last_ind + 2:]#начинаем со след. символа после запятой
print(last)

second_ind=my_favorite_movies.index(',', 11)#ищем вторую запятую после 10 символов
second = my_favorite_movies[12: second_ind]#начинаем сразу после первой запятой и до второй
print(second)

print(my_favorite_movies[-22:-17])
