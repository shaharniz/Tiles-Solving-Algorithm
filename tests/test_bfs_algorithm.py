import unittest
import numpy as np
from tiles_solver.bfs_algorithm import bfs

class TestBFSAlgorithm(unittest.TestCase):
    def test_bfs_with_solvable_state(self):
        initial_state = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]], dtype=np.uint8)
        try:
            bfs(initial_state)
        except Exception as e:
            self.fail(f"bfs() raised an exception unexpectedly: {e}")

    def test_bfs_already_solved(self):
        initial_state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)

        result = bfs(initial_state)

        self.assertEqual(result.algorithm, "BFS")
        self.assertEqual(result.path, [])
        self.assertEqual(result.length, 0)
        self.assertEqual(result.expanded, 0)

    def test_bfs_solution_path_1(self):
        initial_state = np.array([[1, 2, 0], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)

        result = bfs(initial_state)

        self.assertEqual(result.path, ["2", "1"])
        self.assertEqual(result.length, 2)
        self.assertEqual(result.expanded, 2)

    def test_bfs_solution_path_2(self):
        initial_state = np.array([[1, 4, 0], [5, 8, 2], [3, 6, 7]], dtype=np.uint8)

        result = bfs(initial_state)

        self.assertEqual(result.path, ["2", "8", "5", "3", "6", "7", "8", "5", "4", "1"])
        self.assertEqual(result.length, 10)
        self.assertEqual(result.expanded, 357)

    def test_bfs_solution_path_3(self):
        initial_state = np.array([[1, 4, 2], [7, 5, 0], [3, 6, 8]], dtype=np.uint8)

        result = bfs(initial_state)

        self.assertEqual(result.path, ["5", "7", "3", "6", "7", "4", "1"])
        self.assertEqual(result.length, 7)
        self.assertEqual(result.expanded, 69)

    def test_bfs_solution_path_4(self):
        initial_state = np.array([[1, 4, 0], [7, 5, 2], [3, 6, 8]], dtype=np.uint8)

        result = bfs(initial_state)

        self.assertEqual(result.path, ["2", "5", "7", "3", "6", "7", "4", "1"])
        self.assertEqual(result.length, 8)
        self.assertEqual(result.expanded, 130)

    def test_bfs_solution_path_5(self):
        initial_state = np.array([[8, 6, 7], [2, 5, 4], [3, 0, 1]], dtype=np.uint8)

        result = bfs(initial_state)

        self.assertEqual(
            result.path,
            ["5", "4", "1", "5", "4", "6", "8", "2", "3", "4", "6", "8", "2", "3", "4", "6", "8", "1", "7", "2", "1", "7", "5", "8", "7", "4", "3"],
        )
        self.assertEqual(result.length, 27)
        self.assertEqual(result.expanded, 170471)

    def test_bfs_skips_already_explored_state(self):
        initial_state = np.array([[1, 2, 0], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)

        result = bfs(initial_state)

        self.assertLess(result.expanded, 4)


if __name__ == "__main__":
    unittest.main()
