#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Необходимо методом полного перебора решить задачу коммивояжёра. Для начального населенного пункта на построенном
# графе. Оценим время решения данной задачи, так как оно достаточно большое, уменьшим количество узлов и ребер
# графа до 10.

from itertools import permutations


# Матрица расстояний между городами
distance_dict = {
    "Оснабрюк": { aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        "Оснабрюк": 0,
        "Билефельд": 43,
        "Ганновер": 140,
        "Брауншвейг": 167,
        "Магдебург": 353,
        "Галле": float("inf"),
        "Лейпциг": float("inf"),
        "Йена": float("inf"),
        "Эрфурт": float("inf"),
        "Айзенах": 250,
    },
    "Билефельд": {
        "Оснабрюк": 43,
        "Билефельд": 0,
        "Ганновер": 112,
        "Брауншвейг": 210,
        "Магдебург": 300,
        "Галле": float("inf"),
        "Лейпциг": float("inf"),
        "Йена": float("inf"),
        "Эрфурт": float("inf"),
        "Айзенах": float("inf"),
    },
    "Ганновер": {
        "Оснабрюк": 140,
        "Билефельд": 112,
        "Ганновер": 0,
        "Брауншвейг": 68,
        "Магдебург": float("inf"),
        "Галле": float("inf"),
        "Лейпциг": float("inf"),
        "Йена": float("inf"),
        "Эрфурт": float("inf"),
        "Айзенах": float("inf"),
    },
    "Брауншвейг": {
        "Оснабрюк": 167,
        "Билефельд": 210,
        "Ганновер": 68,
        "Брауншвейг": 0,
        "Магдебург": 96,
        "Галле": 76,
        "Лейпциг": 222,
        "Йена": float("inf"),
        "Эрфурт": float("inf"),
        "Айзенах": float("inf"),
    },
    "Магдебург": {
        "Оснабрюк": 353,
        "Билефельд": 300,
        "Ганновер": float("inf"),
        "Брауншвейг": 96,
        "Магдебург": 0,
        "Галле": 76,
        "Лейпциг": 106,
        "Йена": float("inf"),
        "Эрфурт": float("inf"),
        "Айзенах": 240,
    },
    "Галле": {
        "Оснабрюк": float("inf"),
        "Билефельд": float("inf"),
        "Ганновер": float("inf"),
        "Брауншвейг": 76,
        "Магдебург": 76,
        "Галле": 0,
        "Лейпциг": 32,
        "Йена": float("inf"),
        "Эрфурт": float("inf"),
        "Айзенах": float("inf"),
    },
    "Лейпциг": {
        "Оснабрюк": float("inf"),
        "Билефельд": float("inf"),
        "Ганновер": float("inf"),
        "Брауншвейг": 222,
        "Магдебург": 106,
        "Галле": 32,
        "Лейпциг": 0,
        "Йена": 72,
        "Эрфурт": float("inf"),
        "Айзенах": float("inf"),
    },
    "Йена": {
        "Оснабрюк": float("inf"),
        "Билефельд": float("inf"),
        "Ганновер": float("inf"),
        "Брауншвейг": float("inf"),
        "Магдебург": float("inf"),
        "Галле": float("inf"),
        "Лейпциг": 72,
        "Йена": 0,
        "Эрфурт": 50,
        "Айзенах": float("inf"),
    },
    "Эрфурт": {
        "Оснабрюк": float("inf"),
        "Билефельд": float("inf"),
        "Ганновер": float("inf"),
        "Брауншвейг": float("inf"),
        "Магдебург": float("inf"),
        "Галле": float("inf"),
        "Лейпциг": float("inf"),
        "Йена": 50,
        "Эрфурт": 0,
        "Айзенах": 80,
    },
    "Айзенах": {
        "Оснабрюк": 250,
        "Билефельд": float("inf"),
        "Ганновер": float("inf"),
        "Брауншвейг": float("inf"),
        "Магдебург": 240,
        "Галле": float("inf"),
        "Лейпциг": float("inf"),
        "Йена": float("inf"),
        "Эрфурт": 80,
        "Айзенах": 0,
    },
}

# Задаем начальный город
start_city = "Оснабрюк"


def solve_tsp(distance_dict, start_city):
    cities = list(distance_dict.keys())
    n = len(cities)
    start_index = cities.index(start_city)

    # Генерация всех возможных маршрутов (перестановок) кроме начального города
    min_route_length = float("inf")
    best_route = []

    # Генерируем все перестановки всех городов, исключая начальный
    for perm in permutations([i for i in range(n) if i != start_index]):
        route = [start_index] + list(perm) + [start_index]
        route_length = sum(distance_dict[cities[route[i]]][cities[route[i + 1]]] for i in range(n))

        # Обновляем лучший маршрут, если найден маршрут с меньшей длиной
        if route_length < min_route_length:
            min_route_length = route_length
            best_route = [cities[i] for i in route]

    return best_route, min_route_length


if __name__ == "__main__":
    # Выводим лучший маршрут и его длину
    best_route, min_length = solve_tsp(distance_dict, start_city)
    print(f"Лучший маршрут: {' -> '.join(best_route)} с длиной {min_length} км")
