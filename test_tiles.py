import unittest
import numpy as np
from eight_puzzle import EightPuzzle

class TestEightPuzzle(unittest.TestCase):

    def test_valid_initial_state(self):
        initial_state = np.array([[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 0, 8]])
        puzzle = EightPuzzle(initial_state)
        self.assertTrue(np.array_equal(puzzle.state, initial_state))

    def test_invalid_initial_state_shape(self):
        initial_state = np.array([[1, 2, 3],
                                  [4, 5, 6]])
        with self.assertRaises(ValueError):
            EightPuzzle(initial_state)

    def test_invalid_initial_state_type(self):
        initial_state = [[1, 2, 3],
                         [4, 5, 6],
                         [7, 0, 8]]
        with self.assertRaises(TypeError):
            EightPuzzle(initial_state)

    def test_unsolvable_initial_state(self):
        initial_state = np.array([[1, 2, 3],
                                  [4, 6, 5],
                                  [7, 0, 8]])
        with self.assertRaises(ValueError):
            EightPuzzle(initial_state)

    def test_goal_state_check(self):
        goal_state = np.array([[0, 1, 2],
                               [3, 4, 5],
                               [6, 7, 8]])
        puzzle = EightPuzzle(goal_state)
        self.assertTrue(puzzle.check_goal_state())

if __name__ == '__main__':
    unittest.main()