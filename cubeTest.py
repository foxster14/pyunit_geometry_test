import unittest
import cube 

## Since these are all floats & are not rounded at the time of declaration
## The tests will fail if the answer is too specific
class triangleTest(unittest.TestCase):

    def test_area(self):
        assert(cube.surfaceArea(8) == 384)

    def test_volume(self):
        assert(cube.volume(8) == 512)
    
    def test_lateral(self):
        assert(cube.lateralSurfaceArea(8) == 256)

if __name__ == '__main__':
    unittest.main()