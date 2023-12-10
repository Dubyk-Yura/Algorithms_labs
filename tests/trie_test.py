import unittest
from src.trie import build_trie


class TestTrie(unittest.TestCase):
    def test_find_words(self):
        pattern_strings = ["application", "apple", "algo", "battery", "stadium", "console", "lviv"]
        trie = build_trie(pattern_strings)
        result1 = trie.find_word("aplle")
        result2 = trie.find_word("algo")
        result3 = trie.find_word("lviv")
        self.assertEqual(result1, False)
        self.assertEqual(result2, True)
        self.assertEqual(result3, True)

    def test_find_prefix(self):
        pattern_strings = ["application", "apple", "algo", "battery", "stadium", "console", "lviv"]
        trie = build_trie(pattern_strings)
        result1 = trie.find_prefix("app")
        result2 = trie.find_prefix("pbatt")
        result3 = trie.find_prefix("lv")
        self.assertEqual(result1, True)
        self.assertEqual(result2, False)
        self.assertEqual(result3, True)
