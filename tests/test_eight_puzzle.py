import unittest
import numpy as np
from tiles_solver import eight_puzzle


class TestEightPuzzle(unittest.TestCase):

    def test_validate_state_solvability_solvable_state(self):
        state = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]], dtype=np.uint8)  # Inversions count is even => solvable
        self.assertTrue(eight_puzzle.validate_state_solvability(state))

    def test_validate_state_solvability_unsolvable_state(self):
        state = np.array([[1, 2, 3], [4, 6, 5], [7, 0, 8]], dtype=np.uint8)  # Inversions count is odd => unsolvable
        with self.assertRaises(ValueError):
            eight_puzzle.validate_state_solvability(state)

    def test_validate_state_solvability_invalid_shape(self):
        state = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.uint8)  # Shape is not 3x3
        with self.assertRaises(ValueError):
            eight_puzzle.validate_state_solvability(state)

    def test_validate_state_solvability_invalid_type(self):
        state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]  # Not a numpy array
        with self.assertRaises(TypeError):
            eight_puzzle.validate_state_solvability(state)

    def test_validate_state_solvability_invalid_subtype(self):
        state = np.array([[1, "two", 3], [4, 5, 6], [7, 8, 0]])  # Non-integer subtype
        with self.assertRaises(TypeError):
            eight_puzzle.validate_state_solvability(state)

    def test_validate_state_solvability_invalid_digit(self):
        state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.uint8)  # Invalid digit 9
        with self.assertRaises(ValueError):
            eight_puzzle.validate_state_solvability(state)

    def test_validate_state_solvability_duplicate_values(self):
        state = np.array([[1, 2, 3], [4, 5, 6], [7, 7, 0]], dtype=np.uint8)  # Duplicate value 7
        with self.assertRaises(ValueError):
            eight_puzzle.validate_state_solvability(state)

    def test_count_inversions_without_inversions(self):
        state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)
        inversions = eight_puzzle.count_inversions(state)
        self.assertEqual(inversions, 0)

    def test_count_inversions_with_inversions(self):
        state = np.array([[1, 2, 3], [4, 6, 5], [7, 0, 8]], dtype=np.uint8)
        inversions = eight_puzzle.count_inversions(state)
        self.assertEqual(inversions, 1)

    def test_target_state_is_immutable(self):
        with self.assertRaises(ValueError):
            eight_puzzle.TARGET_STATE[0, 0] = 9

    def test_get_actions_as_step(self):
        prev_state = np.array([[1, 2, 3], [4, 0, 5], [6, 7, 8]], dtype=np.uint8)
        new_state = np.array([[1, 2, 3], [0, 4, 5], [6, 7, 8]], dtype=np.uint8)
        step = eight_puzzle._get_action_as_step(prev_state, new_state)
        self.assertEqual(step, "4")

    def test_get_successors_center(self):
        state = np.array([[4, 3, 2], [1, 0, 5], [6, 7, 8]], dtype=np.uint8)
        successor_up = np.array([[4, 0, 2], [1, 3, 5], [6, 7, 8]], dtype=np.uint8)
        successor_down = np.array([[4, 3, 2], [1, 7, 5], [6, 0, 8]], dtype=np.uint8)
        successor_left = np.array([[4, 3, 2], [0, 1, 5], [6, 7, 8]], dtype=np.uint8)
        successor_right = np.array([[4, 3, 2], [1, 5, 0], [6, 7, 8]], dtype=np.uint8)
        np.testing.assert_equal(
            eight_puzzle.get_successors(state),
            {"3": successor_up, "7": successor_down, "1": successor_left, "5": successor_right},
        )

    def test_get_successors_left_edge(self):
        state = np.array([[4, 3, 2], [0, 1, 5], [6, 7, 8]], dtype=np.uint8)
        successor_up = np.array([[0, 3, 2], [4, 1, 5], [6, 7, 8]], dtype=np.uint8)
        successor_down = np.array([[4, 3, 2], [6, 1, 5], [0, 7, 8]], dtype=np.uint8)
        successor_right = np.array([[4, 3, 2], [1, 0, 5], [6, 7, 8]], dtype=np.uint8)
        np.testing.assert_equal(
            eight_puzzle.get_successors(state),
            {"4": successor_up, "6": successor_down, "1": successor_right},
        )

    def test_get_successors_top_right_corner(self):
        state = np.array([[4, 5, 0], [1, 2, 3], [6, 7, 8]], dtype=np.uint8)
        successor_down = np.array([[4, 5, 3], [1, 2, 0], [6, 7, 8]], dtype=np.uint8)
        successor_left = np.array([[4, 0, 5], [1, 2, 3], [6, 7, 8]], dtype=np.uint8)
        np.testing.assert_equal(
            eight_puzzle.get_successors(state),
            {"3": successor_down, "5": successor_left},
        )

    def test_is_goal_valid(self):
        the_goal = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)
        assert eight_puzzle.is_goal(the_goal)

    def test_is_goal_invalid(self):
        not_the_goal = np.array([[3, 4, 5], [0, 1, 2], [6, 7, 8]], dtype=np.uint8)
        assert not eight_puzzle.is_goal(not_the_goal)

    def test_linear_conflicts_heuristic_0(self):
        state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)

        heuristic_value = eight_puzzle.linear_conflicts_heuristic(state)
        # This is the goal state, so both Manhattan distance and linear conflicts are 0

        self.assertEqual(heuristic_value, 0)

    def test_linear_conflicts_heuristic_1(self):
        state = np.array([[0, 2, 1], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)

        heuristic_value = eight_puzzle.linear_conflicts_heuristic(state)
        # Manhattan distance is 2 (tiles 1 and 2 are swapped)
        # There is 1 linear conflict (tiles 1 and 2 in the same row)

        self.assertEqual(heuristic_value, 4)

    def test_linear_conflicts_heuristic_2(self):
        state = np.array([[0, 4, 2], [3, 1, 5], [6, 7, 8]], dtype=np.uint8)

        heuristic_value = eight_puzzle.linear_conflicts_heuristic(state)
        # Manhattan distance is 2 (tiles 1 and 4 are swapped)
        # There is 1 linear conflict (tiles 1 and 4 in the same column)

        self.assertEqual(heuristic_value, 4)

    def test_linear_conflicts_heuristic_3(self):
        state = np.array([[2, 1, 3], [4, 5, 6], [0, 8, 7]], dtype=np.uint8)

        heuristic_value = eight_puzzle.linear_conflicts_heuristic(state)
        # Manhattan distance is 12 (only tile 1 is in the correct position)
        # There are 2 linear conflicts (in rows 0 and 2)

        self.assertEqual(heuristic_value, 16)

    def test_count_conflicts_empty_line(self):
        self.assertEqual(eight_puzzle._count_conflicts([]), 0)

    def test_count_conflicts_single_element(self):
        self.assertEqual(eight_puzzle._count_conflicts([4]), 0)

    def test_count_conflicts_sorted_line(self):
        self.assertEqual(eight_puzzle._count_conflicts([1, 2, 3]), 0)

    def test_count_conflicts_reversed_line(self):
        self.assertEqual(eight_puzzle._count_conflicts([3, 2, 1]), 2)


if __name__ == "__main__":
    unittest.main()
