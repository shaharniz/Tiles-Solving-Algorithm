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


def bfs(initial_state):
    print("Algorithm: BFS")
    EightPuzzle.validate_state_solvability(initial_state)

    root = Node(state=initial_state)
    queue = deque([root])
    explored = set()
    expanded_count = 0

    while queue:
        node = queue.popleft()
        state_key = node.state.tobytes()  # Converting state to bytes for hashing

        if state_key in explored:
            continue

        explored.add(state_key)
        expanded_count += 1

        if EightPuzzle.is_goal(node.state):
            print_path(node)
            print(f"Length: {node.cost}")
            print(f"Expanded: {expanded_count}")
            return

        for step, next_state in EightPuzzle.get_successors(node.state).items():
            child = Node(
                state=next_state,
                parent=node,
                step=step,
                cost=node.cost + 1,
            )
            queue.append(child)


def astar():
    pass
