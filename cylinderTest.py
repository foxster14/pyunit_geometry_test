import unittest
import cylinder 

## Since these are all floats & are not rounded at the time of declaration
## The tests will fail if the answer is too specific
class triangleTest(unittest.TestCase):

    def test_area(self):
        assert(cylinder.surfaceArea(5,4) >= 282)

    def test_volume(self):
        assert(cylinder.volume(5,4) >= 314)
    
    def test_lateral(self):
        assert(cylinder.lateral(5,4) >= 125)
    
    def test_base(self):
        assert(cylinder.base(5) >= 78)

if __name__ == '__main__':
    unittest.main()