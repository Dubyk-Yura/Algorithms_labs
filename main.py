import unittest
from tests.diameter_test import TestDiameter

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(TestDiameter)
    unittest.TextTestRunner().run(test_suite)