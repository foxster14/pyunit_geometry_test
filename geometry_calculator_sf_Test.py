## look up "mock" in the mastering python book to see how to test user input
import unittest
import geometry_calculator_sf as geo
from geometry_calculator_sf import userSelection
from unittest import mock
import sphere

# PyUnit is an object-oriented framework
class selectionMenuTest(unittest.TestCase):
    #@mock.patch('geometry_calculator_sf.input', return_value=8)
    def userInputTest(self):      
        assert(geo.userSelection(8) == 'Invalid selection, please try again.')
        #mocked_input.side_effect = ['8']
        #self.assertTrue(geo.main(),'Invalid selection, please try again.')
        #if input == 8:
            #assert(geo.main() == 'Invalid selection, please try again.')
        #assert(input(8) == 'Invalid selection, please try again.)
    
    def sphereInputTest(self):
        assert(sphere.selection() == userSelection(1))


if __name__ == '__main__':
    unittest.main()