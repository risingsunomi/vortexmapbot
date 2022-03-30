"""
Test generate maps
"""

import unittest
from map_gen import MapGen

class TestMapGen(unittest.TestCase):
    def test_one(self):
        # build simple map
        print('test one')
        mg = MapGen(line_paths=[(1,2), (2,4), (4,8), (8,7), (8,4), (7,5), (5,1), (3,9), (9, 6), (3,6), (7,2)])
        mg.build_plot()

if __name__ == "__main__":
    unittest.main()