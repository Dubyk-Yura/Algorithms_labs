import unittest
from tests.wchains_test import TestWchain

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(TestWchain)
    unittest.TextTestRunner().run(test_suite)
