## look up "mock" in the mastering python book to see how to test user input
import unittest
import geometry_calculator_sf as geo
from unittest import mock

# PyUnit is an object-oriented framework
class selectionMenuTest(unittest.TestCase):
    #@mock.patch('geometry_calculator_sf.input', return_value=8)
    def userInputTest(self, input):
        #mocked_input.side_effect = ['8']
        self.assertTrue(geo.main(),'Invalid selection, please try again.')
        if input == 8:
            assert(geo.main() == 'Invalid selection, please try again.')
        #assert(input(8) == 'Invalid selection, please try again.)

if __name__ == '__main__':
    unittest.main()