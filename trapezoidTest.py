import unittest
import trapezoid 

class trapezoidTest(unittest.TestCase):

    def test_area(self):
        # Seeing if expected output when 4 is given as inputmatches actual output
        assert(trapezoid.area(4,5,4) == 18.0)

    def test_median(self):
        assert(trapezoid.median(4,5) == 4.5)

if __name__ == '__main__':
    unittest.main()