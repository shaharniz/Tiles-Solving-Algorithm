import unittest
import numpy as np
from tiles_solver.search_utils import Node, SearchResult, build_path, expand_node


class TestSearchUtils(unittest.TestCase):
    def test_build_path_returns_steps_in_root_to_leaf_order(self):
        root = Node(state=np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.uint8))
        child = Node(state=root.state, parent=root, step="4", cost=1)
        grandchild = Node(state=root.state, parent=child, step="7", cost=2)

        self.assertEqual(build_path(grandchild), ["4", "7"])

    def test_expand_node_returns_list_of_child_nodes(self):
        state = np.array([[1, 2, 3], [4, 0, 5], [6, 7, 8]], dtype=np.uint8)
        node = Node(state=state)

        children = expand_node(node)

        self.assertIsInstance(children, list)
        self.assertEqual(len(children), 4)
        self.assertTrue(all(isinstance(child, Node) for child in children))
        self.assertTrue(all(child.parent is node for child in children))
        self.assertTrue(all(child.cost == 1 for child in children))

    def test_search_result_stores_algorithm_outcome(self):
        result = SearchResult(algorithm="BFS", path=["1", "2"], length=2, expanded=3)

        self.assertEqual(result.algorithm, "BFS")
        self.assertEqual(result.path, ["1", "2"])
        self.assertEqual(result.length, 2)
        self.assertEqual(result.expanded, 3)
