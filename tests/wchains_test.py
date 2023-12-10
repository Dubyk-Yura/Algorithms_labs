import unittest
from src.wchain import find_max_sequence_words, dict_of_words, list_of_words


class TestWchain(unittest.TestCase):
    def test_default_condition(self):
        find_max_sequence_words(dict_of_words, list_of_words)
        with open("src/wchain.out.txt", "r", encoding="utf-8") as wchain_out:
            result = int(wchain_out.readline())
        self.assertEqual(result, 6)
