import unittest
from astar import find_path, h

class TestAstar(unittest.TestCase):

    def test_h(self):
        self.assertEqual(h([3, 3], [2, 2]), 2)

    def test_astar(self):
        grid = [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
        ]
        path = find_path((3,3), (0, 0), grid)
        self.assertEqual(path, [[3, 2], [3, 1], [2, 1], [2, 0], [1, 0], [0, 0]])

if __name__ == '__main__':
    unittest.main()
