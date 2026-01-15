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

    def test_count_inversions(self):
        initial_state = np.array([[0, 1, 2],
                                  [3, 4, 5],
                                  [6, 7, 8]])
        puzzle = EightPuzzle(initial_state)
        inversions = puzzle.count_inversions()
        self.assertEqual(inversions, 0)

    def test_get_possible_actions_center(self):
        initial_state = np.array([[4, 3, 2],
                                  [1, 0, 5],
                                  [6, 7, 8]])
        puzzle = EightPuzzle(initial_state)
        assert puzzle.get_possible_actions() == {'UP', 'DOWN', 'LEFT', 'RIGHT'}

    def test_get_possible_actions_left_edge(self):
        initial_state = np.array([[4, 3, 2],
                                  [0, 1, 5],
                                  [6, 7, 8]])
        puzzle = EightPuzzle(initial_state)
        assert puzzle.get_possible_actions() == {'UP', 'DOWN', 'RIGHT'}

    def test_get_possible_actions_top_right_corner(self):
        initial_state = np.array([[4, 5, 0],
                                  [1, 2, 3],
                                  [6, 7, 8]])
        puzzle = EightPuzzle(initial_state)
        assert puzzle.get_possible_actions() == {'DOWN', 'LEFT'}

    def test_valid_transition(self):
        initial_state = np.array([[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 0, 8]])
        puzzle = EightPuzzle(initial_state)
        new_state = puzzle.transition('UP')
        expected_state = np.array([[1, 2, 3],
                                   [4, 0, 6],
                                   [7, 5, 8]])
        self.assertTrue(np.array_equal(new_state, expected_state))
        
    def test_invalid_transition(self):
        initial_state = np.array([[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 0, 8]])
        with self.assertRaises(IndexError):
            EightPuzzle(initial_state).transition('DOWN')
        

if __name__ == '__main__':
    unittest.main()