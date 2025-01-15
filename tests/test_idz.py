#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest


sys.path.append("../src")
from idz import distance_dict, solve_tsp


class TestTSPSolver(unittest.TestCase):
    def test_optimal_route(self):
        """Тестирование оптимального маршрута"""
        start_city = "Оснабрюк"
        best_route, min_length = solve_tsp(distance_dict, start_city)

        # Проверяем, что начальный и конечный города совпадают
        self.assertEqual(best_route[0], start_city, "Маршрут должен начинаться с начального города")
        self.assertEqual(best_route[-1], start_city, "Маршрут должен заканчиваться начальным городом")

        # Проверяем, что маршрут покрывает все города
        all_cities = list(distance_dict.keys())
        self.assertCountEqual(best_route[:-1], all_cities, "Маршрут должен покрывать все города ровно один раз")

    def test_no_infinite_routes(self):
        """Убедимся, что функция обрабатывает маршруты с бесконечными расстояниями"""
        start_city = "Оснабрюк"
        best_route, min_length = solve_tsp(distance_dict, start_city)

        # Проверяем, что длина маршрута конечна
        self.assertNotEqual(min_length, float("inf"), "Длина маршрута не должна быть бесконечной")

    def test_small_graph(self):
        """Тестирование на небольшом графе"""
        small_distance_dict = {
            "A": {"A": 0, "B": 1, "C": 2},
            "B": {"A": 1, "B": 0, "C": 1},
            "C": {"A": 2, "B": 1, "C": 0},
        }
        start_city = "A"
        best_route, min_length = solve_tsp(small_distance_dict, start_city)

        # Проверяем ожидаемый результат
        self.assertEqual(best_route, ["A", "B", "C", "A"], "Маршрут для небольшого графа неверный")
        self.assertEqual(min_length, 4, "Длина маршрута для небольшого графа неверная")


if __name__ == "__main__":
    unittest.main()
