import unittest
from src.city_without_gas import cities_without_gas


class TestGasInCities(unittest.TestCase):
    def test_with_condition_data(self):
        city_list = ["Lviv", "Dnipro", "Kyiv", "Zhytomyr", "Ternopil", "Odesa"]
        gas_stores_list = ["gas_1", "gas_2"]
        active_gas_pipelines_list = [
            ["gas_1", "Kyiv"],
            ["gas_2", "Lviv"],
            ["Kyiv", "Ternopil"],
            ["Kyiv", "Dnipro"],
            ["Lviv", "Ternopil"],
            ["Lviv", "Zhytomyr"],
            ["Dnipro", "Zhytomyr"],
            ["Ternopil", "Dnipro"],
            ["Odesa", "Ternopil"],
        ]
        result = cities_without_gas(
            city_list, gas_stores_list, active_gas_pipelines_list
        )
        self.assertEqual(
            result, [["gas_1", ["Lviv", "Odesa"]], ["gas_2", ["Kyiv", "Odesa"]]]
        )

    def test_with_no_pipelines(self):
        city_list = ["Lviv", "Dnipro", "Kyiv", "Zhytomyr", "Ternopil", "Odesa"]
        gas_stores_list = ["gas_1", "gas_2"]
        active_gas_pipelines_list = []
        result = cities_without_gas(
            city_list, gas_stores_list, active_gas_pipelines_list
        )
        self.assertEqual(
            result,
            [
                ["gas_1", ["Lviv", "Dnipro", "Kyiv", "Zhytomyr", "Ternopil", "Odesa"]],
                ["gas_2", ["Lviv", "Dnipro", "Kyiv", "Zhytomyr", "Ternopil", "Odesa"]],
            ],
        )

    def test_with_all_pipelines(self):
        city_list = ["Lviv", "Dnipro", "Kyiv", "Zhytomyr", "Ternopil", "Odesa"]
        gas_stores_list = ["gas_1", "gas_2"]
        active_gas_pipelines_list = [
            ["gas_1", "Kyiv"],
            ["gas_2", "Lviv"],
            ["Kyiv", "Ternopil"],
            ["Kyiv", "Dnipro"],
            ["Kyiv", "Lviv"],
            ["Lviv", "Kyiv"],
            ["Lviv", "Ternopil"],
            ["Lviv", "Zhytomyr"],
            ["Lviv", "Odesa"],
            ["Dnipro", "Zhytomyr"],
            ["Ternopil", "Dnipro"],
            ["Odesa", "Ternopil"],
        ]
        result = cities_without_gas(
            city_list, gas_stores_list, active_gas_pipelines_list
        )
        self.assertEqual(result, [["gas_1", []], ["gas_2", []]])
