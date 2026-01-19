import unittest
import numpy as np
from eight_puzzle import EightPuzzle, Actions


class TestEightPuzzle(unittest.TestCase):

    def test_validate_state_solvability_solvable_state(self):
        state = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]], dtype=np.uint8)
        self.assertTrue(EightPuzzle.validate_state_solvability(state))

    def test_validate_state_solvability_invalid_shape(self):
        state = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.uint8)
        with self.assertRaises(ValueError):
            EightPuzzle.validate_state_solvability(state)

    def test_validate_state_solvability_invalid_type(self):
        state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        with self.assertRaises(TypeError):
            EightPuzzle.validate_state_solvability(state)

    def test_validate_state_solvability_invalid_digit(self):
        state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.uint8)
        with self.assertRaises(ValueError):
            EightPuzzle.validate_state_solvability(state)

    def test_validate_state_solvability_invalid_subtype(self):
        state = np.array([[1, "two", 3], [4, 5, 6], [7, 8, 0]])
        with self.assertRaises(TypeError):
            EightPuzzle.validate_state_solvability(state)

    def test_validate_state_solvability_duplicate_values(self):
        state = np.array([[1, 2, 3], [4, 5, 6], [7, 7, 0]], dtype=np.uint8)
        with self.assertRaises(ValueError):
            EightPuzzle.validate_state_solvability(state)

    def test_validate_state_solvability_unsolvable_state(self):
        state = np.array([[1, 2, 3], [4, 6, 5], [7, 0, 8]], dtype=np.uint8)
        with self.assertRaises(ValueError):
            EightPuzzle.validate_state_solvability(state)

    def test_count_inversions(self):
        state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)
        inversions = EightPuzzle.count_inversions(state)
        self.assertEqual(inversions, 0)

    def test_get_successors_center(self):
        state = np.array([[4, 3, 2], [1, 0, 5], [6, 7, 8]], dtype=np.uint8)
        successor_up = np.array([[4, 0, 2], [1, 3, 5], [6, 7, 8]], dtype=np.uint8)
        successor_down = np.array([[4, 3, 2], [1, 7, 5], [6, 0, 8]], dtype=np.uint8)
        successor_left = np.array([[4, 3, 2], [0, 1, 5], [6, 7, 8]], dtype=np.uint8)
        successor_right = np.array([[4, 3, 2], [1, 5, 0], [6, 7, 8]], dtype=np.uint8)
        np.testing.assert_equal(
            EightPuzzle.get_successors(state),
            {
                Actions.UP: successor_up,
                Actions.DOWN: successor_down,
                Actions.LEFT: successor_left,
                Actions.RIGHT: successor_right,
            },
        )

    def test_get_successors_left_edge(self):
        state = np.array([[4, 3, 2], [0, 1, 5], [6, 7, 8]], dtype=np.uint8)
        successor_up = np.array([[0, 3, 2], [4, 1, 5], [6, 7, 8]], dtype=np.uint8)
        successor_down = np.array([[4, 3, 2], [6, 1, 5], [0, 7, 8]], dtype=np.uint8)
        successor_right = np.array([[4, 3, 2], [1, 0, 5], [6, 7, 8]], dtype=np.uint8)
        np.testing.assert_equal(
            EightPuzzle.get_successors(state),
            {
                Actions.UP: successor_up,
                Actions.DOWN: successor_down,
                Actions.RIGHT: successor_right,
            },
        )

    def test_get_successors_top_right_corner(self):
        state = np.array([[4, 5, 0], [1, 2, 3], [6, 7, 8]], dtype=np.uint8)
        successor_down = np.array([[4, 5, 3], [1, 2, 0], [6, 7, 8]], dtype=np.uint8)
        successor_left = np.array([[4, 0, 5], [1, 2, 3], [6, 7, 8]], dtype=np.uint8)
        np.testing.assert_equal(
            EightPuzzle.get_successors(state),
            {
                Actions.DOWN: successor_down,
                Actions.LEFT: successor_left,
            },
        )

    def test_is_goal_valid(self):
        the_goal = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)
        assert EightPuzzle.is_goal(the_goal)

    def test_is_goal_invalid(self):
        not_the_goal = np.array([[3, 4, 5], [0, 1, 2], [6, 7, 8]], dtype=np.uint8)
        assert not EightPuzzle.is_goal(not_the_goal)

if __name__ == "__main__":
    unittest.main()
