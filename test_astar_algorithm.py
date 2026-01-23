import unittest
from unittest.mock import patch
from io import StringIO
import numpy as np
from astar_algorithm import astar

silence = patch("sys.stdout", new_callable=StringIO)  # Decorator to silence test prints

class TestAStarAlgorithm(unittest.TestCase):

    # @silence
    # def test_astar_with_solvable_state(self, _):
    #     initial_state = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]], dtype=np.uint8)
    #     try:
    #         astar(initial_state)
    #     except Exception as e:
    #         self.fail(f"bfs() raised an exception unexpectedly: {e}")

    # @silence
    # def test_astar_with_unsolvable_state(self, _):
    #     initial_state = np.array([[1, 2, 3], [5, 4, 6], [0, 7, 8]], dtype=np.uint8)
    #     with self.assertRaises(ValueError):
    #         astar(initial_state)
    
    # @silence
    # def test_astar_with_invalid_state_shape(self, _):
    #     initial_state = np.array(
    #         [[1, 2, 3], [4, 5, 6]], dtype=np.uint8
    #     )  # Invalid shape
    #     with self.assertRaises(ValueError):
    #         astar(initial_state)

    # @silence
    # def test_astar_with_invalid_state_type(self, _):
    #     initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]  # Not a numpy array
    #     with self.assertRaises(TypeError):
    #         astar(initial_state)

    # @silence
    # def test_astar_with_invalid_state_subtype(self, _):
    #     initial_state = np.array(
    #         [[1, 2, 3], [4, 5, 6], [0, 7, 8]], dtype=np.int32
    #     )  # Non-uint8 subtype
    #     with self.assertRaises(TypeError):
    #         astar(initial_state)

    # @silence
    # def test_astar_with_invalid_digit(self, _):
    #     initial_state = np.array(
    #         [[1, 2, 3], [4, 5, 6], [0, 7, 9]], dtype=np.uint8
    #     )  # Invalid digit 9
    #     with self.assertRaises(ValueError):
    #         astar(initial_state)

    # @silence
    # def test_astar_with_duplicate_values(self, _):
    #     initial_state = np.array(
    #         [[1, 2, 3], [4, 5, 6], [0, 7, 7]], dtype=np.uint8
    #     )  # Duplicate value 7
    #     with self.assertRaises(ValueError):
    #         astar(initial_state)

    # @silence
    # def test_astar_already_solved(self, mock_stdout):
    #     self.maxDiff = None  # Shows full prints diff on failure
    #     initial_state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)
        
    #     expectet_output_lines = [
    #         "Algorithm: A*",
    #         "Path: ",
    #         "Length: 0",
    #         "Expanded: 0",
    #     ]
        
    #     astar(initial_state)
    #     actual_output_lines = mock_stdout.getvalue().strip().split("\n")

    #     self.assertEqual(actual_output_lines, expectet_output_lines)

    # @silence
    # def test_astar_solution_path_1(self, mock_stdout):
    #     self.maxDiff = None  # Shows full prints diff on failure
    #     initial_state = np.array([[1, 2, 0], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)
        
    #     expectet_output_lines = [
    #         "Algorithm: A*",
    #         "Path: ",
    #         "Length: ",
    #         "Expanded: ",
    #     ]
        
    #     astar(initial_state)
    #     actual_output_lines = mock_stdout.getvalue().strip().split("\n")

    #     self.assertEqual(actual_output_lines, expectet_output_lines)

    # @silence
    # def test_astar_solution_path_2(self, mock_stdout):
    #     self.maxDiff = None  # Shows full prints diff on failure
    #     initial_state = np.array([[1, 4, 0], [5, 8, 2], [3, 6, 7]], dtype=np.uint8)
        
    #     expectet_output_lines = [
    #         "Algorithm: A*",
    #         "Path: ",
    #         "Length: ",
    #         "Expanded: ",
    #     ]
        
    #     astar(initial_state)
    #     actual_output_lines = mock_stdout.getvalue().strip().split("\n")

    #     self.assertEqual(actual_output_lines, expectet_output_lines)

    # @silence
    # def test_astar_solution_path_3(self, mock_stdout):
    #     self.maxDiff = None  # Shows full prints diff on failure
    #     initial_state = np.array([[1, 4, 2], [7, 5, 0], [3, 6, 8]], dtype=np.uint8)
        
    #     expectet_output_lines = [
    #         "Algorithm: A*",
    #         "Path:",
    #         "Length: ",
    #         "Expanded: ",
    #     ]
        
    #     astar(initial_state)
    #     actual_output_lines = mock_stdout.getvalue().strip().split("\n")

    #     self.assertEqual(actual_output_lines, expectet_output_lines)

    # @silence
    # def test_astar_solution_path_4(self, mock_stdout):
    #     self.maxDiff = None  # Shows full prints diff on failure
    #     initial_state = np.array([[1, 4, 0], [7, 5, 2], [3, 6, 8]], dtype=np.uint8)
        
    #     expectet_output_lines = [
    #         "Algorithm: A*",
    #         "Path: ",
    #         "Length: ",
    #         "Expanded: ",
    #     ]
        
    #     astar(initial_state)
    #     actual_output_lines = mock_stdout.getvalue().strip().split("\n")

    #     self.assertEqual(actual_output_lines, expectet_output_lines)


if __name__ == "__main__":
    unittest.main()
