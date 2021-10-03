import unittest
import cuboid

class triangleTest(unittest.TestCase):

    def test_area(self):
        assert(cuboid.surface(5,6,7) == 214)

    def test_volume(self):
        assert(cuboid.volume(5,6,7) == 210)
    
    def test_lateral(self):
        assert(cuboid.lateral(5,6,7) == 154)

if __name__ == '__main__':
    unittest.main()