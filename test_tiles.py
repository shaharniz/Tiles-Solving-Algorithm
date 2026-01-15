import unittest
import numpy as np
from eight_puzzle import EightPuzzle, Directions

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
        assert puzzle.get_possible_actions() == {Directions.UP, Directions.DOWN, Directions.LEFT, Directions.RIGHT}

    def test_get_possible_actions_left_edge(self):
        initial_state = np.array([[4, 3, 2],
                                  [0, 1, 5],
                                  [6, 7, 8]])
        puzzle = EightPuzzle(initial_state)
        assert puzzle.get_possible_actions() == {Directions.UP, Directions.DOWN, Directions.RIGHT}

    def test_get_possible_actions_top_right_corner(self):
        initial_state = np.array([[4, 5, 0],
                                  [1, 2, 3],
                                  [6, 7, 8]])
        puzzle = EightPuzzle(initial_state)
        assert puzzle.get_possible_actions() == {Directions.DOWN, Directions.LEFT}

    def test_valid_transition(self):
        initial_state = np.array([[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 0, 8]])
        puzzle = EightPuzzle(initial_state)
        puzzle.transition(Directions.UP)
        expected_state = np.array([[1, 2, 3],
                                   [4, 0, 6],
                                   [7, 5, 8]])
        self.assertTrue(np.array_equal(puzzle.state, expected_state))
        
    def test_invalid_transition(self):
        initial_state = np.array([[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 0, 8]])
        with self.assertRaises(ValueError):
            EightPuzzle(initial_state).transition(Directions.DOWN)
        
    def test_total_cost_counting(self):
        initial_state = np.array([[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 0, 8]])
        puzzle = EightPuzzle(initial_state)
        puzzle.transition(Directions.UP)
        puzzle.transition(Directions.UP)
        puzzle.transition(Directions.LEFT)

        assert puzzle._total_cost == 3

if __name__ == '__main__':
    unittest.main()