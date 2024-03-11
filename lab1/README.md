# 00

## Задание


У нас есть словарь sites, который содержит координаты городов. Каждый город представлен как ключ в словаре и его координаты из двух элементов (x, y):

```python
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
```
У нас также есть пустой словарь distances, куда мы будем записывать расстояния между каждой парой городов.

```python
distances = {}
```

## Решение:
* Мы проходимся по каждому городу первый раз и создаем в словаре distances пустой словарь для текущего города city1.
* Затем мы извлекаем координаты (x, y) для текущего города city1.
* Далее мы проходимся по каждому городу второй раз.
* Извлекаем координаты (x, y) для второго города city2.
* Рассчитываем расстояние между city1 и city2 используя формулу Евклидового расстояния: ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
* Записываем это расстояние в словарь distances для пары city1 и city2.
* Повторяем шаги с 3 по 6 для всех возможных комбинаций городов.
* В итоге distances будет содержать расстояния между всеми парами городов.
* Выводим полученные расстояния.
```python
for city1 in sites:
    distances[city1] = {}
    x1, y1 = sites[city1]

    for city2 in sites:
        x2, y2 = sites[city2]
        distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        distances[city1][city2] = distance

print(distances)
```

## Результат
![im1](https://github.com/Lemka6ix/Python/blob/main/lab1/images/00.png)

# 01

## Задание

Есть значение радиуса круга
```python
radius = 42
```
Выведите на консоль значение площади этого круга с точностю до 4-х знаков после запятой. Далее, пусть есть координаты двух точек _point_1 = (23, 34)_ и _point_2 = (30, 30)_. Если точка _point_1_ лежит внутри того самого круга _[центр в начале координат (0, 0), radius = 42]_, то выведите на консоль _True_, или _False_, если точка лежит вовне круга, и аналогично проверить _point_2_.

## Решение
* Фомула площади круга = пи * радиус в квадрате
```python
S = round(math.pi * radius**2, 4)
print(S)
```

* Далее мы объявляем функцию ins_curcle(point, radius), которая принимает точку point в формате (x, y) и радиус круга radius.
* Разбиваем координаты точки на x и y: x, y = point.
* Находим расстояние от точки до центра координат (0, 0) с помощью формулы расчета расстояния между двумя точками в прямоугольной системе координат: \[ \sqrt{x^2 + y^2} \]. Здесь мы используем функцию math.sqrt, чтобы вычислить квадратный корень.
* Функция возвращает результат сравнения найденного расстояния с радиусом круга: return distance <= radius. Если расстояние до точки меньше или равно радиусу, функция вернет True, что означает, что точка находится внутри круга, иначе вернется False, что обозначает, что точка находится вне круга.
```python
def ins_curcle(point, radius):
    x, y = point
    distance = math.sqrt(x**2 + y**2) #Расстояние от точки до центра
    return distance <= radius
print(ins_curcle(point_1, radius))
print(ins_curcle(point_2, radius))
```

## Резуьтат
![im2](https://github.com/Lemka6ix/Python/blob/main/lab1/images/01.png)


# 02

## Задание
Расставьте знаки операций "плюс", "минус", "умножение" и скобки между числами "1 2 3 4 5" так, чтобы получилось число "25". Использовать нужно только указанные знаки операций, но не обязательно все перечесленные. Порядок чисел нужно сохранить.
## Решение
```python
res = 1 * 2 + 3 + 4 * 5
print(res)
```
## Результат
![imss](https://github.com/Lemka6ix/Python/blob/main/lab1/images/02.png)


# 03

## Задание
Есть строка с перечислением фильмов
```python
my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
```
Выведите на консоль с помощью индексации строки, последовательно:
* первый фильм
* последний
* второй
* второй с конца

Запятая не должна выводиться. Переопределять _my_favorite_movies_ нельзя. Использовать _.split()_ или _.find()_ или другие методы строки нельзя - пользуйтесь только срезами, как указано в задании!

## Решение
```python
first = my_favorite_movies[:10]
print(first)
```
* Используем срез [:10], чтобы взять подстроку с начала строки до 10-го символа. Это дает нам первый фильм.

```python
last_ind = my_favorite_movies.rindex(',') #rindex возвращает наибольший индекс, по которому обнаруживается конец указанной подстроки в исходной
last = my_favorite_movies[last_ind + 2:]#начинаем со след. символа после запятой
print(last)
```
* Ищем последнюю запятую в строке методом rindex().
* Далее мы берем подстроку, начиная с символа после найденной запятой до конца строки.

```python
second_ind=my_favorite_movies.index(',', 11)
second = my_favorite_movies[12: second_ind]
print(second)
```
* Здесь ищем индекс второй запятой, начиная с 11-го символа в строке.
* Далее берем подстроку, начиная с 12-го символа (после первой запятой) до индекса второй запятой.

```python
print(my_favorite_movies[-22:-17])
```


## Результат
![sssss](https://github.com/Lemka6ix/Python/blob/main/lab1/images/03.png)


# 04

## Задание
Создайте списки:
```python
my_family = []
```
```python
my_family_height = [
    # ['имя', рост],
]
```
Выведите на консоль рост отца в формате:

_Рост отца - ХХ см_;

Выведите на консоль общий рост вашей семьи как сумму ростов всех членов:

_Общий рост моей семьи - ХХ см_.

## Решение
```python
#   Рост отца - ХХ см
father_height = [person[1] for person in my_family_height if person[0] == 'Папа'][0]
print(f'Рост отца - {father_height} см')
#   Общий рост моей семьи - ХХ см
total_height = sum([person[1] for person in my_family_height])
print(f'Общий рост моей семьи - {total_height} см')
```
* father_height = [person[1] for person in my_family_height if person[0] == 'Папа'][0]
   - Данное выражение использует генератор списков для создания списка всех ростов членов семьи, где каждый рост извлекается из элемента person в my_family_height.
   - Условие if person[0] == 'Папа' фильтрует только те элементы, где имя человека равно 'Папа'.
   - Затем [1] используется для извлечения только роста из соответствующего элемента.

* total_height = sum([person[1] for person in my_family_height])
   - Эта строка создает сумму всех значений роста в списке my_family_height с помощью генератора списков.
   - [person[1] for person in my_family_height] извлекает все значения роста из списка.
   - sum(...) используется для нахождения суммы всех ростов.
## Результат
![pedd](https://github.com/Lemka6ix/Python/blob/main/lab1/images/04.png)



# 05

## Задание
Есть список животных в зоопарке 
```python
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
```
Посадите медведя (bear) между львом и кенгуру; добавьте птиц из списка birds в последние клетки зоопарка 
`birds = ['rooster', 'ostrich', 'lark', ]`; уберите слона; выведите на консоль в какой клетке сидит лев _(lion)_ и жаворонок _(lark)_. Номера при выводе должны быть понятны простому человеку, не программисту.

## Решение
* С помощью метода `insert` добавляем элемент _bear_ на позицию с индексом 1 в список _zoo_. В результате _bear_ будет вставлен после _lion_, таким образом изменяя порядок элементов в списке.
* С помощью метода `extend` добавляем все элементы из списка _birds_ в конец списка _zoo_. В результате в списке _zoo_ будут все животные и птицы.
* `lioncage = zoo.index('lion') + 1`: c помощью метода remove удаляет первый элемент в списке zoo со значением 'elephant'.
* `larkcage = zoo.index('lark') + 1`: Далее находим индекс 'lion' в списке zoo и добавляем 1, чтобы получить номер клетки для льва. Индексы в списке начинаются с 0, но по смыслу для пользователя клетки нумеруются с 1.
* Аналогично находим индекс 'lark' в списке zoo и добавляем 1 для определения клетки, в которой находится жаворонок.
## Результат
![deds](https://github.com/Lemka6ix/Python/blob/main/lab1/images/05.png)



# 06

## Задание
* Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут. Точность указывается в функции `round(a, b)`, где __a__, это число которое надо округлить, а __b__ количество знаков после запятой.
```python
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
```
распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате: 

_Три песни звучат ХХХ.XX минут_

Обратите внимание, что делать много вычислений внутри print() - плохой стиль. Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz).

* Есть словарь песен группы Depeche Mode:
```python
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
```
Распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress' в формате:

_А другие три песни звучат ХХХ минут_

## Решение
```python
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

total_time = sum([song[1] for song in violator_songs_list if song[0] in ['Halo', 'Enjoy the Silence', 'Clean']])
print(f'Три песни звучат {total_time:.2f} минут')

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

total_time_other = sum(violator_songs_dict[song] for song in ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'])
print(f'А другие три песни звучат {total_time_other:.2f} минут')
```

* `total_time = sum([song[1] for song in violator_songs_list if song[0] in ['Halo', 'Enjoy the Silence', 'Clean']])`: Используем `list comprehension` для создания списка длительностей песен из `violator_songs_list`, если название песни находится в списке `['Halo', 'Enjoy the Silence', 'Clean']`. Затем мы суммируем все значения в этом списке, чтобы получить общее время игры этих трёх песен.
> `List comprehension` в Python — это мощный и компактный способ создания списков на основе существующих последовательностей (списков, строк, кортежей и др.) с использованием более лаконичного синтаксиса. Синтаксис list comprehension выглядит следующим образом:
```python
new_list = [выражение for элемент in последовательность if условие]
```
>> выражение: это операция или выражение, которое будет применено к каждому элементу.

>> элемент: переменная, которая принимает значение из последовательности.

>> последовательность: исходная последовательность, по которой происходит итерация.

>> условие (необязательно): это предикат, который фильтрует элементы. Только элементы, для которых условие истинно, попадают в новый список.

* `total_time_other = sum(violator_songs_dict[song] for song in ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'])`: Здесь суммируем длительности песен `'Sweetest Perfection'`, `'Policy of Truth'` и `'Blue Dress'`, используя их значения из словаря `violator_songs_dict`.

## Результат
![dsdsdd](https://github.com/Lemka6ix/Python/blob/main/lab1/images/06.png)



# 07

## Задание
Есть зашифрованное сообщение:
```python
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
```
Нужно его расшифровать и вывести на консоль в удобочитаемом виде. Должна получиться фраза на русском языке, например: как два байта переслать.

## Решение
```python
word1 = secret_message[0][3]
word2 = secret_message[1][9:13]
word3 = secret_message[2][5:15:2]
word4 = secret_message[3][12:6:-1]
word5 = secret_message[4][20:15:-1]

mess = f'{word1} {word2} {word3} {word4} {word5}' #С помощю f'' ставятся пробелы между словами
print(mess)
```

* Извлекаем символ с индексом 3 из первого элемента secret_message. Это поможет нам получить первое слово.
* Извлекаем подстроку с индексами от 9 до 12 (не включая 13) из второго элемента secret_message. Это даст нам второе слово.
* Извлекаем символы с индексами от 5 до 14 с шагом 2 из третьего элемента secret_message. Это поможет нам получить третье слово.
* Извлекаем символы с индексами от 12 до 6 в обратном порядке из четвёртого элемента secret_message. Это даст нам четвёртое слово.
* Извлекаем символы с индексами от 20 до 15 в обратном порядке из пятого элемента secret_message. Это поможет нам получить пятое слово.
* Комбинируем отдельные слова в одну строку с пробелами между ними, используя обратные кавычки (f-string) для форматирования строки
## Результат
![shgjkv](https://github.com/Lemka6ix/Python/blob/main/lab1/images/07.png)


# 08

## Задание
* В саду сорвали цветы:
```python
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )`
```
* На лугу сорвали цветы
```python
`meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )`
```
* Создайте множество цветов, произрастающих в саду и на лугу
`garden_set =`
`meadow_set =`
* Выведите на консоль все виды цветов
* Выведите на консоль те, которые растут и там и там
* Выведите на консоль те, которые растут в саду, но не растут на лугу
* Выведите на консоль те, которые растут на лугу, но не растут в саду

## Решение
```python
garden_set = set(garden)
meadow_set = set(meadow)
all_flowers = garden_set.union(meadow_set)
print("Все виды:", all_flowers)
tutitam = garden_set.intersection(meadow_set)
print("И там и там: ", tutitam)
gardenonly = garden_set.difference(meadow_set)
print("Только в саду: ", gardenonly)
meadowonly = meadow_set.difference(garden_set)
print("Только на лугу: ", meadowonly)
```
* Cоздается множество `garden_set` из кортежа `garden`. Функция `set()` удаляет дубликаты и формирует уникальный набор элементов, произрастающих в саду.
* Аналогично создается множество `meadow_set` из кортежа meadow, представляющего цветы, произрастающие на лугу.
* Метод `union()` объединяет два множества `garden_set` и `meadow_set`, чтобы получить все уникальные цветы из обоих множеств.
* Метод `intersection()` находит пересечение двух множеств `garden_set` и `meadow_set`, т.е. цветы, которые есть и там и там.
* Метод `difference()` находит разницу между множествами `garden_set` и `meadow_set`, то есть цветы, которые есть только в саду.  Аналогично, метод `difference()` находит цветы, которые есть только на лугу.
> `set()` - это функция, которая создает множество (set) из итерируемого объекта, такого как список, кортеж или строка.
> ```python
> my_list = [1, 2, 2, 3, 3, 4]
> my_set = set(my_list)
> print(my_set)  # Выведет: {1, 2, 3, 4}```
## Результат
![nccvcbg](https://github.com/Lemka6ix/Python/blob/main/lab1/images/08.png)


# 09

## Задание
Есть словарь магазинов c распродажами:
```python
shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}
```
Создайте словарь цен на продкты следующего вида (писать прямо в коде):
```python
sweets = {
    'название сладости': [
        {'shop': 'название магазина', 'price': 99.99},
        # TODO тут с клавиатуры введите магазины и цены (можно копипастить ;)
    ],
    # TODO тут с клавиатуры введите другую сладость и далее словарь магазинов
}
```
Указать надо только по 2 магазина с минимальными ценами.

## Решение
```python
sweets = {
    'мармелад': [
        {'shop': 'пятерочка', 'price': 15.99},
        {'shop': 'ашан', 'price': 19.99}
    ],
    'шоколад': [
        {'shop': 'магнит', 'price': 49.99},
        {'shop': 'пятерочка', 'price': 52.99}
    ],
    'вата': [
        {'shop': 'пятерочка', 'price': 5.99},
        {'shop': 'магнит', 'price': 6.99}
    ]
}
```



# 10

## Задание
Есть словарь кодов товаров:
```python
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
```
Есть словарь списков количества товаров на складе:
```python
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
```
Рассчитать на какую сумму лежит каждого товара на складе.
__Например__, для ламп:
```python
lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
```
Или проще (/сложнее ?):
```python
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')
```

## Решение
```python
# Для столов
table_code = goods['Стол']
table_quantity = store[table_code][0]['quantity'] + store[table_code][1]['quantity']
table_cost = store[table_code][0]['quantity'] * store[table_code][0]['price'] + store[table_code][1]['quantity'] * store[table_code][1]['price']
print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')

# Для диванов
sofa_code = goods['Диван']
sofa_quantity = store[sofa_code][0]['quantity'] + store[sofa_code][1]['quantity']
sofa_cost = store[sofa_code][0]['quantity'] * store[sofa_code][0]['price'] + store[sofa_code][1]['quantity'] * store[sofa_code][1]['price']
print('Диван -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')

# Для стульев
chair_code = goods['Стул']
chair_quantity = store[chair_code][0]['quantity'] + store[chair_code][1]['quantity'] + store[chair_code][2]['quantity']
chair_cost = store[chair_code][0]['quantity'] * store[chair_code][0]['price'] + store[chair_code][1]['quantity'] * store[chair_code][1]['price'] + store[chair_code][2]['quantity'] * store[chair_code][2]['price']
print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')
```
* Извлекаем код товара для стола из словаря goods.
* Вычисляем общее количество столов на складе, суммируя количество столов из двух различных записей в словаре store.
* Вычисляем общую стоимость всех столов на складе, умножая количество каждого типа столов на его цену и складывая их.

* Извлекаем код товара для дивана из словаря goods.
* Вычисляем общее количество диванов на складе.
* Вычисляем общую стоимость всех диванов на складе.

* Извлекаем код товара для стульев из словаря goods.
* Вычисляем общее количество стульев на складе.
* Вычисляем общую стоимость всех стульев на складе.

## Результат
![rar](https://github.com/Lemka6ix/Python/blob/main/lab1/images/10.png)

_____

# Ссылки на используемые материалы
* https://clck.ru/MfEMS
* https://www.programiz.com/python-programming
* https://youtu.be/Rpf63XT5XLI?si=IJ60tBQVwI3X-i4E
