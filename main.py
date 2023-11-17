import unittest
from tests.gas_test import TestGasInCities

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(TestGasInCities)
    unittest.TextTestRunner().run(test_suite)
