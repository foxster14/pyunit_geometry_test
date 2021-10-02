## look up "mock" in the mastering python book to see how to test user input
import unittest
import geometry_calculator_sf as geo

# PyUnit is an object-oriented framework
class add3Test(unittest.TestCase):

    def test_add3(self):
        # Seeing if expected output when 4 is given as inputmatches actual output
        assert(geo.add3(4) == 7)

if __name__ == '__main__':
    unittest.main()