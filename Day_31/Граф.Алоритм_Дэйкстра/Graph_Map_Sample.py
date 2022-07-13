# -*- coding: utf-8 -*-
# Алгоритм Дэйкстра поиска кратчайшего расстояния. Асимптотика: O(N**2)

# Требования: веса - НЕ отрицательные числа (ноль допускается).
# Цель: поиск кратчейшего расстояния от исходной вершины 'start_node' к вершине 'target_node'.

# Схема маршрутов находится в файле Map_Sample.png

import sys # для отпределения величины бесконечности sys.maxsize

from rich import print


class Graph:

    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        """
        Метод обеспечивает симметричность графа.
        """
        graph = dict()
        for n in nodes:
            graph[n] = {}
        # Методом update() обновляем словарь. Если пара ключ-значение отсутствует, то вносим в словарь, иначе
        # заменяем значение при совпадение ключа.
        graph.update(init_graph)

        # симметричность графа
        for node, edges in graph.items():
            for node2, value in edges.items():
                # if graph[node2].get(node, False) == False:
                if not graph[node2].get(node, False): # поиск ключа методом get(), если ключа нет, то присваивает ключу значение False
                    graph[node2][node] = value
        return graph

    def get_nodes(self):
        """
        Метод возвращает узлы графа.
        """
        return self.nodes

    def get_outgoing_edges(self, node):
        """
        Метод возвращает соседей узла.
        """
        connection = []
        for n in self.nodes:
            # if self.graph[node].get(n, False) != False:
            if self.graph[node].get(n, False): # поиск ключа методом get(), если ключа нет, то присваивает ключу значение False
                connection.append(n)
        return connection

    def value(self, node1, node2):
        """
        Метод возвращает значение ребра между двумя узлами графа.
        """
        if node1 not in self.nodes or node2 not in self.nodes:
            print('Дороги не существует.')
            raise KeyError('Дороги не существует.')
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    """
    Функция поиска кратчайшего пути от начальной точки до всех точек графа.
    """
    unvisited_nodes = graph.get_nodes() # получает узлы графа
    shortest_path = {} # известное время в пути до каждого из узлов
    previous_nodes = {} # хранит траекторию текущего пути для каждого узла
    max_value = sys.maxsize # значение "бесконечность"

    # поставим время в пути до каждого узла равное бесконечности
    for node in unvisited_nodes:
        if node == start_node:
            shortest_path[node] = 0 # у начального города поставим значение 0
        else:
            shortest_path[node] = max_value

    while unvisited_nodes:
        current_min_node = None # сосед с минимальным временем в пути до него

        # пройдем циклом по всем путям, найдём соседа до которого ближе всего и запишем его в current_min_node
        for node in unvisited_nodes: # находим ближайшего соседа
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]: # проверяем, путь до следующего соседа короче, чем путь до ранее выбранного?
                current_min_node = node

        neighbours = graph.get_outgoing_edges(current_min_node) # получаем соседей соседа
        for n in neighbours:
            # расстояние до города = цифра около города + значение дороги
            tentative_value = shortest_path[current_min_node] + \
                              graph.value(current_min_node, n)

            if tentative_value < shortest_path[n]:
                shortest_path[n] = tentative_value # обновляем расстояние до города
                previous_nodes[n] = current_min_node # обновим лучший путь к текущему городу

        unvisited_nodes.remove(current_min_node) # забываем посещенный город

    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    """
    Функция вывода данных.
    """
    path = []
    node = target_node # текущий город при поиске пути

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
    path.append(start_node)

    print(f"Найден лучший маршрут из '{start_node}' в '{target_node}':")
    # print(" <- ".join(path)) # движение в обратную сторону
    print(" -> ".join(path[::-1])) # для движение вперед можно развернуть список и стрелочку 
    print("Время в пути:", shortest_path[target_node], 'ч.') # время между узлами в часах


# ############################################# ТЕСТИРОВАНИЕ #############################################################

# # стартовая точка
# start_node = 'Казань'

# # пункт назначения
# target_node = 'Зеленодольск'

# # добавление имен узлов в виде списка
# nodes = ['Москва', 'Уфа', 'Казань', 'Зеленодольск', 'Владивосток']

# # добавление весов узлам (время в пути до узла) 
# init_graph = {'Казань': {'Москва': 8, 'Зеленодольск': 1, 'Уфа': 10}, # дороги из Казани до Москвы, Зеленодольска, Уфы
#               'Москва': {'Уфа': 15, 'Казань': 8},                    # дороги из Москвы до Уфы, Казани
#               'Владивосток': {'Уфа': 101}}                           # дорога из Владивостока до Уфы

# # добавление графа
# g = Graph(nodes, init_graph)

# # построение графа
# """OUT:
# Граф:
# {'Москва': {'Уфа': 15, 'Казань': 8}, 'Уфа': {'Москва': 15, 'Казань': 10, 'Владивосток': 101},
# 'Казань': {'Москва': 8, 'Зеленодольск': 1, 'Уфа': 10}, 'Зеленодольск': {'Казань': 1},
# 'Владивосток': {'Уфа': 101}}
# """
# print(f'Граф:\n{g.graph}')

# # получение узлов (используется в алгоритме для нахождения unvisited_nodes)
# """OUT:
# Узлы:
# ['Москва', 'Уфа', 'Казань', 'Зеленодольск', 'Владивосток']
# """
# print(f'Узлы:\n{g.get_nodes()}')

# # получение соседей узла
# """OUT:
# Соседние узлы:
# ['Москва', 'Уфа', 'Зеленодольск']
# """
# print(f'Соседние узлы:\n{g.get_outgoing_edges(start_node)}')

# # получение расстояние между двумя узлами
# print(f'Время в пути: {g.value(start_node, target_node)} ч.') # OUT: Время в пути: 1 ч.
# # print(g.value('Казань', 'Зеленодольс')) # OUT: Дороги не существует.
# # print(g.value('Казан', 'Зеленодольск')) # OUT: Дороги не существует.

#########################################################################################################################

# Пример 1
# Схема маршрутов находится в файле Map_Sample.png

# Входные данные:
start_node = 'Уфа' # стартовкая точка
target_node = 'Зеленодольск' # пункт назначения
nodes = ['Москва', 'Уфа', 'Казань', 'Зеленодольск', 'Владивосток'] # имена узлов в виде списка

# добавление весов узлам (время в пути до узла) 
init_graph = {'Казань': {'Москва': 8, 'Зеленодольск': 1, 'Уфа': 10}, # дороги из Казани до Москвы, Зеленодольска, Уфы
              'Москва': {'Уфа': 15, 'Казань': 8},                    # дороги из Москвы до Уфы, Казани
              'Владивосток': {'Уфа': 101}}                           # дорога из Владивостока до Уфы

# добавление графа
g = Graph(nodes, init_graph)

# Выходные данные:
previous_nodes, shortest_path = dijkstra_algorithm(g, start_node) # запускаем алгоритм Дэйкстра
# print(previous_nodes)
# print(shortest_path)
print_result(previous_nodes, shortest_path, start_node, target_node) # вывод результата

# Пример 2
# Схема маршрутов находится в файле Map_Sample.png

# Входные данные:
start_node = 'Москва' # стартовкая точка
target_node = 'Владивосток' # пункт назначения
nodes = ['Москва', 'Уфа', 'Казань', 'Зеленодольск', 'Владивосток'] # имена узлов в виде списка

# добавление весов узлам (время в пути до узла) 
init_graph = {'Казань': {'Москва': 8, 'Зеленодольск': 1, 'Уфа': 10}, # дороги из Казани до Москвы, Зеленодольска, Уфы
              'Москва': {'Уфа': 15, 'Казань': 8},                    # дороги из Москвы до Уфы, Казани
              'Владивосток': {'Уфа': 101}}                           # дорога из Владивостока до Уфы

# добавление графа
g = Graph(nodes, init_graph)

# Выходные данные:
previous_nodes, shortest_path = dijkstra_algorithm(g, start_node) # запускаем алгоритм Дэйкстра
# print(previous_nodes)
# print(shortest_path)
print_result(previous_nodes, shortest_path, start_node, target_node) # вывод результата
