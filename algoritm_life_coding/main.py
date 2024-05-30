

user = input('Введите имя: ')

a = []
b = []
c = []

if user[0].lower() == 'a':
    a.append(user)
    print(f'a: {a}')
elif user[0].lower() == 'b':
    b.append(user)
    print(f'b: {b}')
elif user[0].lower() == 'c':
    c.append(user)
    print(f'c: {c}')
else:
    print('Введите корректные имена, начинающиеся с букв a, b или c')
#---#

'''
massiv
'''

numbers = [1, 2, 1, 4, 3, 22]


def linear_search(list_numbers, item):

    for index, element in enumerate(list_numbers):
        if element == item:
            return f'Элемент - {element}, находиться под индексом - {index}'
    return -1


print(linear_search(numbers, int(input('Введите число которую вы ищете: '))))

'''
array - Массив
Пишем функцию - binary_search
Функция binary_search получает отсортированный массив и значение.
Если значение присутствует в массиве,
то функция возвращает его позицию.
При этом мы должны следить за тем,
в какой части массива производиться поиск.
Вначале это весь массив:
'''
item = list(input('Введите числа: '))

low = 0
high = len(list) - 1

# Каждый раз алгоритм проверяет средний элемент
mid = (low + high) / 2
guess = list[mid]
# Полный код выглядит так:

def binary_search(searching_list, item):
    # В переменных low and high хранятся границы той части поиска, в которой выполняется поиск
    low = 0
    high = len(searching_list)-1

    while low <= high:  # пока это часть не сократиться до минимума
        mid = (low + high) // 2  # проверяем средний элемент
        guess = searching_list[mid]

        if guess == item:  # Значение найдено
            return f'Значение {item} - находиться по индексу {mid}'
        if guess > item:  # Много
            high = mid - 1

        else:  # Мало
            low = mid + 1

    return 'Такого элемента в списке Нет!'  # Значение не существует



res = list(range(1, 20))  # А теперь тестируем функцию


print(binary_search(res, int(input('Введите число которую ищете в списке: '))))




def binary_search(list_, my_number):
    low = 0
    high = len(list_) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list_[mid]
        if guess == my_number:
            return f'Значение {my_number} находится под индексом {mid}'
        elif guess < my_number:
            low = mid + 1
        else:
            high = mid - 1

    return 'Такого элемента НЕТ!'

numbers = [3, 1, 2, 3, 4]  # Список должен быть отсортирован перед использованием
print(binary_search(numbers, int(input('Введите число, которое хотите найти: '))))
#---#

def search_binary(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return (f'{item} находиться под индексом - {mid}')
        elif guess < item:
            return 'Вы попали выше диапазона'

        else:
            high = mid - 1


    return 'Неправильные данные'

res = list(range(1, 20))

print(search_binary(res, int(input('Введите число: '))))


'''
O(log(n))
'''
import random


xodi = int(input('Введите ваши ходы: '))
random_number = random.randint(1, 100)

while xodi >= 0:
    user = int(input('Введите число(1, 100): '))

    xodi -= 1
    if xodi == 0:
        print(f'Вы проиграли!, осталось {xodi} ходов')
        break
    print(f'У вас осталось {xodi} - ходов!')


    if user == random_number:
        print('Вы выйграли')
        break

    elif user > random_number:
        print('Меньше')

    elif user < random_number:
        print('Больше')

    else:
        print('Введена неверная операция')


'''
array
'''
array = ('d', [1.1, 2.2, 3.3], 6)

for i in array:
    print(i)

'''
list
'''
lists = [1.1, 2.2, 3.3]

for i in lists:
    print(i)
#---#

'''
Сортировка выбором
'''

def findSmallest(arr):
    min_el = arr[0]  # Для хранения наименьшего значения
    smallest_index = 0  # Для хоранения индекса наименьшего значения

    for i in range(1, len(arr)):
        if arr[i] < min_el:
            min_el = arr[i]
            smallest_index = i
    return smallest_index

# Теперь на основе этой функций можно написать функцию сортировки выбором:

def selectionSort(arr):  # Соритирует массив
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)  # Находит наименьший элемент в массиве
        newArr.append(arr.pop(smallest))  # и добавляет его в новый массив

    return newArr

print(selectionSort([2, 1, 3, 4, 5]))
#---#

'''
Рекурсия
'''

def look_for_key(main_box):
    empty = []
    pile = main_box.make_a_pile_to_look_thourgh()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                return 'fount the key'

# Второй способ основан на рекурсии - Рекурсией называется вызыв фнукций самой себя

def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)  # Рекурсия
        elif item.is_a_key():
            print('found the key!')
#---#


#---#

'''
Не заускай этот код! ;)
'''
# def count(i):
#     print(i)
#     count(i - 1)

# count(5)
#---#


# def countdown(i):
#     print(i)
#     if i <= 1:
#         return
#     else:
#         countdown(i-1)

# countdown(5)

# Такая же функция идентичный как предыдущей но, с циклом while!

# def countdown(i):
#     while i >= 1:
#         i -= 1
#         print(i)


# countdown(5)
#---#

name = input('Введите свое имя: ')
age = 19

if name == 'Нуртилек':
    print('Вы', name, 'Ты красавчик!')
elif name == 'Асад':
    print('Вы', name, 'Ты Асад')

else:
    print('Вы введи нечто другое!')

import webbrowser

url = 'https://www.youtube.com/'

I_am = input('Введите ваш запрос: ')
if I_am == 'Открой ютуб':
    webbrowser.open(url)

else:
    print('всегда к вашим услугам сэр!')
#---#

'''
Стэк вызовов
'''
def greet(name):
    print(f'Hello {name}!')
    greet2(name)
    print('Getting ready to say by...')
    bye()

def greet2(name):
    print('How are you?', name)

def bye():
    print('Ok bye!')


greet('Asadullah')

# 2
def greet(name):
    print('hello from job!')
    greet2(name)
    print('getting ready bye')
    bye()

def greet2(name):
    print('Hello', name)

def bye():
    print('bye bye!')


greet('Asadullah')
#---#

'''
factorial - recursies
'''

def factorial(x):
    if x == 1:
        return 1

    return x * factorial(x - 1)



print(factorial(3))
#---#

'''
просуммировать все числа и вернуть сумму
'''
# def sum(arr):
#     total = 0
#     for i in arr:
#         total += i
#
#     return total
#
#
# print(sum([1, 2, 3, 4, 5]))
#---#

'''
Упражнение 4.1
Напишите код для функций sum
'''
# Мое решение:
# def func_sum(x):
#     if x == int:
#         return x
#     else:
#         return sum(x)
#
# print(func_sum([1, 2, 3, 4, 5]))

# Решение книги:
# def sum(list):
#     if list == []:
#         return 0
#     return list[0] + sum(list[1:])
#
#
# print(sum([1, 2, 3, 4, 5]))
#---#

'''
Напишите рекурсивную функцию для подсчета элементов в списке
'''
# Мое решение(Не работает):
# def count_elements_list(list):
#     counter = 0
#     for el in list:
#         return count_elements_list(counter + el)
#
#     return counter
#
# print(count_elements_list([1, 2, 3, 4]))

# Решение книги:
# def count(list):
#     if list == []:  # Базовый случай(обьязательно должен присутсвовать в рекурсивной функций)
#         return 0
#     return 1 + count(list[1:])
#
# print(count([1, 2, 3, 4, 5]))
#---#

'''
Найдите наибольшее число в списке
'''
# Мой вариант
# def max_el_list(lst):
#     first_el = lst[0]
#     for i in range(len(lst)):
#         if lst[i] > first_el:
#             first_el = lst[i]
#
#     return first_el
#
# print(min_el_list([4, 5, 2, 1]))

# Вариант книги(Очень краткий и рабочий, кстати):
# def max_el(lst):
#     if len(lst) == 2:
#         return lst[0] if lst[0] > lst[1] else lst[1]
#     sub_max = max_el(lst[1:])
#     return sub_max if sub_max > lst[0] else lst[0]
#
# print(max_el([4, 5, 6, 2, 1]))
#---#

'''
Сортировка массивов
'''
# def sort_array(arr):
#     if len(arr) < 2:
#         return arr

#     mid = len(arr) // 2
#     left_half = sort_array(arr[:mid])
#     right_half = sort_array(arr[mid:])

#     return merge(left_half, right_half)

# def merge(left, right):
#     sorted_array = []
#     while left and right:
#         if left[0] <= right[0]:
#             sorted_array.append(left.pop(0))
#         else:
#             sorted_array.append(right.pop(0))

#     sorted_array.extend(left)
#     sorted_array.extend(right)

#     return sorted_array

# print(sort_array([2, 1, 4, 3]))
#---#

# def sort_arr(arr):
#     mid = len(arr) // 2
#     left_el = sort_arr(arr[:mid])
#     right_el = sort_arr(arr[mid:])

#     sort_list = []

#     if left_el > right_el:
#         left_el = right_el
#         sort_list.append(left_el[:mid])
#     else:
#         sort_list.append(right_el[mid:])

#     return sort_list

# print(sort_arr([3, 2, 5, 4, 1]))
#---#

'''
Вот как выглядет программный код быстрой сортировки:
'''
# def quicksort(array):
#     if len(array) < 2:  # Базовый случай: массивы с 0 и 1 элементов уже отсортированы
#         return array
#     else:
#         pivot = array[0]  # Рекурсивный случай
#         less = [i for i in quicksort(array[1:]) if i < pivot]  # Подмассив всех элементов меньших опорного

#         greater = [i for i in array[1:] if i > pivot]  # Подмассив всех элементов больших опорного

#         return quicksort(less) + [pivot] + quicksort(greater)

# print(quicksort([5, 2, 3, 1, 4]))
#---#

'''
Таблица умножение(умножение на каждый элемент массива)
'''
# def table(arr):

#     if len(arr) < 2:
#         return arr

#     result = []
#     for i in arr:
#         result.append(i * i)

#     return result

# print(table([2, 3, 7, 8, 9 , 10]))
#---#

'''
Хэш-функция на примере кода. Получаем строку и возравщаем число
'''
# def hashe(dictatory, my):
#     if my in dictatory:
#         return dictatory[my]
#     return 'Такого ключа нет в словаре!'


# dict_ = {
#     'asad': 18,
#     'muza': 19,
# }

# res = hashe(dictatory=dict_, my=18)

# print(res)

'''
Ваш код не является хэш-функцией в классическом понимании. Хэш-функция — это функция, которая преобразует входные данные (часто строки) в фиксированное значение (обычно число), которое затем используется для быстрого поиска данных в структурах данных, таких как хэш-таблицы.

Ваш код просто проверяет наличие ключа в словаре и возвращает соответствующее значение. Это не хэш-функция, а функция поиска в словаре.

Корректное название для вашего кода может быть:

"Функция поиска в словаре. Получаем строку (ключ) и возвращаем число (значение)".

Если вам нужно использовать настоящую хэш-функцию, вы можете воспользоваться встроенной функцией hash в Python:
'''
# def example_hash_function(input_string):
#     return hash(input_string)

# print(example_hash_function("asad"))
'''
Этот код берет строку и возвращает её хэш-значение, что больше соответствует понятию хэш-функции.
'''
#---#

'''
Хэш-таблицы в Python(dict)
'''

# book = dict()

# book['apple'] = 0.67
# book['avacado'] = 1.49
# book['milk'] = 2.21

# print(book['apple'])
#---#

'''
Исключение дуликатов
'''
# voted = {}

# def check_voted(name):
#     if voted.get(name):
#         print('Kick them out!')
#     else:
#         voted[name] = True
#         print('let them vote!')

# check_voted('tom')
# check_voted('asadullah')
# check_voted('tom')
#---#

'''
Кэш:
Оказываеться Кэш который сохраняет обработанные данные Веб-страницы на SSD-диске хранится в хэше 
'''

# cache = {}

# def get_cache_url(url):
#     if cache.get(url):
#         return cache[url]  # Возвращаються кэшируемые данные
#     else:
#         data = get_data_from_server(url)
#         cache[url] = data  # Данные сначало сохранаяються в кэше
#         return data
#---#

'''
Реализация графа
'''
# graph = {}

# graph['you'] = ['alise', 'bob', 'clier']

# print(graph['you'])

'''
Граф - всего лишь набор узлов и ребер, 
поэтому для представления графа на Python ничего больше не потребуеться.
А как насчет большего графа ?
'''
# graph = {}
# graph['you'] = ['alice', 'bob', 'clier']
# graph['bob'] = ['anuj', 'peggy']
# graph['alice'] = ['peggy']
# graph['anuj'] = []
# graph['thom'] = []
# graph['johny'] = []


# print(graph)
#---#

'''
Реализация алгоритма поиска в ширину а графе
'''


# graph = {}
# graph['you'] = ['alice', 'bob', 'clier']

# from collections import deque
# search_queue = deque()  # Создание новой очереди
# search_queue += graph['you']

# def person_is_seller(name):
#     return name[-1] == 'm'

# def search_shirina(graph):
#     while search_queue:  # Пока очередь пуста
#         person = search_queue.popleft()  # ... из очереди извлекаеться первый человек
#         if person_is_seller(person):  # Поверяем являеться ли этот человек продавцом манго
#             print(person + "is a mango seller!")  # Да, это продавец манго
#             return True
#         else:
#             search_queue += graph[person]  # Нет, не являеться. Все его(он - который не является продавцом манго, так как это так, мы ищем у его друзей, есть продавец манго) друзья добавляються в очередь поиска
#     return False  # Если очередь дошла до этой строки, то продвацов манго у наших всех контактов нет!
#---#

'''
Чтоб проверить ближайшего соседа надо сделать кое моменты:
Не повторять проверку на уже проверенном соседе!
'''

graph = {}
graph['you'] = ['alice', 'bob', 'clier']
graph['clier'] = ['tom', 'jonny']
graph['bob'] = ['anuj', 'peggy']
graph['peggy'] = []
graph['alice'] = ['peggy', 'i_mangom']
graph['i_mangom'] = []
graph['anuj'] = []
graph['tom'] = []
graph['jonny'] = []

from collections import deque
search_queue = deque()  # Создание новой очереди
search_queue += graph['you']


# # Пишем функцию для продавцов манго
def person_seller_mango(name):
    return 'mangom' in name

# Теперь пишем код для поиска в ширину(находим продавца манго)
def search_seller_mango(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # Этот массив используется для отслеживания уже проверенных людей
    while search_queue:
        person = search_queue.popleft()
        if not person in search_queue:  # Человек проверяться только в том случае, если он не проверился
            if person_seller_mango(person):
                print(person, 'Продавец манго!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)  # Человек помечаеться как уже проверенный
    print('Нет продавцов манго!')
    return False



search_seller_mango('you')

'''
Усовершение предыдущего кода:
'''

from collections import deque

# # Создаем граф
graph = {
    'you': ['alice', 'bob', 'clier'],
    'clier': ['tom', 'jonny'],
    'bob': ['anuj', 'peggy'],
    'peggy': [],
    'alice': ['peggy', 'i_mango'],
    'i_mango': [],
    'anuj': [],
    'tom': [],
    'jonny': []
}

# # Обновляем функцию для проверки продавца манго
def person_seller_mango(name):
    return 'mango' in name

# Теперь пишем код для поиска в ширину (находим продавца манго)
def search_seller_mango(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # Этот массив используется для отслеживания уже проверенных людей
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:  # Человек проверяется только в том случае, если он не проверялся ранее
            if person_seller_mango(person):
                print(person, 'Продавец манго!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)  # Человек помечается как уже проверенный
    print('Нет продавцов манго!')
    return False

# Запуск поиска
search_seller_mango('you')
#---#

'''
Реалиация алгоритма дейкстры
Будет и обновленная версия с низу теущей.
'''
graph = {}
graph['start'] = {}  # Инициализируем вложенный словарь для ключа 'start'
graph['start']['a'] = 6
graph['start']['b'] = 2

# Включим в граф остальные узлы и их соседей
graph['a'] = {}
graph['a']['finish'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['finish'] = 5
graph['finish'] = {}  # У конечного узла нет соседей

print(graph['a'])
#---#

'''
infinity - В Python - Это бесконечность, продолжаем алгоритм дейктсры
'''

import math

positive_infinity = math.inf
negative_infinity = -math.inf

'''
Пишем алгоритм Дейкстры - на примере настоящего кода, взвешиваем все и делаем все идеально
'''

graph = {}
graph['start'] = {}  # Инициализируем вложенный словарь для ключа 'start'
graph['start']['a'] = 6
graph['start']['b'] = 2

# Включим в граф остальные узлы и их соседей
graph['a'] = {}
graph['a']['finish'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['finish'] = 5
graph['finish'] = {}  # У конечного узла нет соседей


infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['finish'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['in'] = None

# Наконец нам нужен массив для отслеживания всех уже обработанных узлов, так как один узел не должен обрабатываться многократно
processed = []

'''
Определяем функцию find_lowest_cost_node - Который обрабатывает кто меньше а кто больше стоит
'''
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # Перебрать все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # Если это узел с наименьшей стоимостью из уже виденных и он еще не был обработан...
            lowest_cost = cost  # ...он назначаеться новым узлом с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node


# Code:
node = find_lowest_cost_node(costs)  # Найти узел с наименьшей стоимостью среди необработанных
while node is not None:  # Если обработаны все узлы, цикл while завершен
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # Перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # Если к соседу можно быстрее добраться через теущий узел...
            costs[n] = new_cost  # ...обновить стоимость для этого узла
            parents[n] = node  # Этот узел становиться новым родителем для соседа
    processed.append(node)  # Узел помечается как обработанный
    node = find_lowest_cost_node(costs)  # Найти следующий узел для обработки и повторить цикл


print(find_lowest_cost_node(parents['a']))


'''
Обновленный, работающий код:
'''
# Инициализация графа
graph = {
    'start': {'a': 6, 'b': 2},
    'a': {'finish': 1},
    'b': {'a': 3, 'finish': 5},
    'finish': {}
}

# Инициализация стоимости узлов
infinity = float('inf')
costs = {
    'a': 6,
    'b': 2,
    'finish': infinity
}

# Инициализация родителей узлов
parents = {
    'a': 'start',
    'b': 'start',
    'finish': None
}

# Массив для отслеживания обработанных узлов
processed = []

# Функция для нахождения узла с наименьшей стоимостью
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Алгоритм Дейкстры
def dijkstra():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

# Запуск алгоритма
dijkstra()

# Вывод результатов
def print_shortest_path():
    node = 'finish'
    path = []
    while node != 'start':  # Продолжать пока не достигнем начального узла
        if node is None:
            print("Путь не найден")
            return
        path.append(node)
        node = parents[node]
    path.append('start')
    path.reverse()
    print("Кратчайший путь:", ' -> '.join(path))
    print("Стоимость пути до финиша:", costs['finish'])

print_shortest_path()
#---#

'''
Жадные алгоритмы
'''

states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# Список станций, из которого будет выбираться покрытие, Восользуемся хэшем
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

# Структура данных для храниения итогового набора станций
final_stations = set()

# Создем переменную для хранения многоохватываемых станций

while states_needed:
    best_stations = None
    states_covered = set()
    for station, states_for_station in stations.items():  # Цикл for перебирает все станций и находит среди них наилучщую
        covered = states_needed & states_for_station  # Новый синтаксис! Это операция называется "пересичением множеств"
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    final_stations.add(best_station)
    states_needed -= states_covered

# Остается вывести содержимое final_stations:
print(final_stations)


'''
Обьяснение пересичений:

set_1 = {1, 2, 3}
set_2 = {3, 5, 6}

print(set_1 & set_2)

-----------------------

Обьяснение add:
st = {'a', 'b', 'c'}
st.add('e')

print(st)
'''

































