import unittest
import cone

class triangleTest(unittest.TestCase):

    def test_slant(self):
        assert(cone.slant(3,4) == 5)

    def test_surfaceArea(self):
        assert(cone.surface(3,4) >= 75)

    def test_volume(self):
        assert(cone.volume(3,4) >= 37)
    
    def test_lateral(self):
        assert(cone.lateral(3,4) >= 47)

if __name__ == '__main__':
    unittest.main()