import unittest
from tests.trie_test import TestTrie

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(TestTrie)
    unittest.TextTestRunner().run(test_suite)
