from collections import deque
from eight_puzzle import EightPuzzle


class Node:
    def __init__(self, state, parent=None, step=None, cost=0):
        self.state = state
        self.parent = parent
        self.step = step
        self.cost = cost


def print_path(node):
    path = []
    while node:
        if node.step is not None:
            path.append(node.step)
        node = node.parent
    path.reverse()
    print("Path:", " ".join(path))


def expand_node(node):
    expanded_node_queue = deque()
    for step, next_state in EightPuzzle.get_successors(node.state).items():
        child = Node(
            state=next_state,
            parent=node,
            step=step,
            cost=node.cost + 1,
        )
        expanded_node_queue.append(child)

    return expanded_node_queue
