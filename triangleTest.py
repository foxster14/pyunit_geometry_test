import unittest
import triangle 

class triangleTest(unittest.TestCase):

    def test_area(self):
        assert(triangle.surfaceArea(6,4,4,4) == 6.93)

    ## This  test will fail because the math.sqrt returns a float
    ## and the answer isn't rounded until printed to screen
    def test_semi_perimeter(self):
        assert(triangle.semiPerimeter(12) == 6)
    
    def test_perimeter(self):
        assert(triangle.perimeter(4,4,4) == 12)

if __name__ == '__main__':
    unittest.main()