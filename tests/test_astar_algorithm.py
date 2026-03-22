import unittest
import numpy as np
from unittest.mock import patch
from tiles_solver.astar_algorithm import astar
from tiles_solver.search_utils import Node

class TestAStarAlgorithm(unittest.TestCase):
    def test_astar_with_solvable_state(self):
        initial_state = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]], dtype=np.uint8)
        try:
            astar(initial_state)
        except Exception as e:
            self.fail(f"astar() raised an exception unexpectedly: {e}")

    def test_astar_already_solved(self):
        initial_state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)

        result = astar(initial_state)

        self.assertEqual(result.algorithm, "A*")
        self.assertEqual(result.path, [])
        self.assertEqual(result.length, 0)
        self.assertEqual(result.expanded, 0)

    def test_astar_solution_path_1(self):
        initial_state = np.array([[1, 2, 0], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)

        result = astar(initial_state)

        self.assertEqual(result.path, ["2", "1"])
        self.assertEqual(result.length, 2)
        self.assertEqual(result.expanded, 2)

    def test_astar_solution_path_2(self):
        initial_state = np.array([[1, 4, 0], [5, 8, 2], [3, 6, 7]], dtype=np.uint8)

        result = astar(initial_state)

        self.assertEqual(result.path, ["2", "8", "5", "3", "6", "7", "8", "5", "4", "1"])
        self.assertEqual(result.length, 10)
        self.assertEqual(result.expanded, 10)

    def test_astar_solution_path_3(self):
        initial_state = np.array([[1, 4, 2], [7, 5, 0], [3, 6, 8]], dtype=np.uint8)

        result = astar(initial_state)

        self.assertEqual(result.path, ["5", "7", "3", "6", "7", "4", "1"])
        self.assertEqual(result.length, 7)
        self.assertEqual(result.expanded, 9)

    def test_astar_solution_path_4(self):
        initial_state = np.array([[1, 4, 0], [7, 5, 2], [3, 6, 8]], dtype=np.uint8)

        result = astar(initial_state)

        self.assertEqual(result.path, ["2", "5", "7", "3", "6", "7", "4", "1"])
        self.assertEqual(result.length, 8)
        self.assertEqual(result.expanded, 10)

    def test_astar_solution_path_5(self):
        initial_state = np.array([[8, 6, 7], [2, 5, 4], [3, 0, 1]], dtype=np.uint8)

        result = astar(initial_state)

        self.assertEqual(
            result.path,
            ["5", "4", "1", "5", "4", "6", "8", "2", "3", "4", "6", "8", "2", "3", "4", "6", "8", "1", "7", "2", "1", "7", "5", "8", "7", "4", "3"],
        )
        self.assertEqual(result.length, 27)
        self.assertEqual(result.expanded, 2372)

    def test_astar_expands_shared_state_only_once(self):
        start = np.array([0], dtype=np.uint8)
        left = np.array([1], dtype=np.uint8)
        right = np.array([2], dtype=np.uint8)
        shared = np.array([3], dtype=np.uint8)
        goal = np.array([4], dtype=np.uint8)

        expansion_counts = {
            start.tobytes(): 0,
            left.tobytes(): 0,
            right.tobytes(): 0,
            shared.tobytes(): 0,
        }

        def fake_expand(node):
            state_key = node.state.tobytes()
            expansion_counts[state_key] += 1

            if np.array_equal(node.state, start):
                return [
                    Node(state=left, parent=node, step="L", cost=node.cost + 1),
                    Node(state=right, parent=node, step="R", cost=node.cost + 1),
                ]
            if np.array_equal(node.state, left):
                return [Node(state=shared, parent=node, step="S", cost=node.cost + 1)]
            if np.array_equal(node.state, right):
                return [Node(state=shared, parent=node, step="T", cost=node.cost + 1)]
            if np.array_equal(node.state, shared):
                return [Node(state=goal, parent=node, step="G", cost=node.cost + 1)]

            self.fail("A* attempted to expand an unexpected state")

        with patch("tiles_solver.astar_algorithm.expand_node", side_effect=fake_expand), \
             patch("tiles_solver.astar_algorithm.is_goal", side_effect=lambda state: np.array_equal(state, goal)), \
             patch("tiles_solver.astar_algorithm.linear_conflicts_heuristic", return_value=0):
            result = astar(start, validate=False)

        self.assertEqual(result.path, ["L", "S", "G"])
        self.assertEqual(result.length, 3)
        self.assertEqual(result.expanded, 4)
        self.assertEqual(expansion_counts[shared.tobytes()], 1)


if __name__ == "__main__":
    unittest.main()
