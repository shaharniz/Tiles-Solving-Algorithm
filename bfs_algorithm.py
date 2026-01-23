from collections import deque
from eight_puzzle import EightPuzzle
from search_utils import Node, print_path, expand_node


def bfs(initial_state):
    print("Algorithm: BFS")
    EightPuzzle.validate_state_solvability(initial_state)

    if EightPuzzle.is_goal(initial_state):
        print("Path: ")
        print("Length: 0")
        print("Expanded: 0")
        return

    root = Node(state=initial_state)
    queue = deque([root])
    explored = set()
    expanded_count = 0

    while queue:
        node = queue.popleft()
        state_key = node.state.tobytes()  # Converting to bytes for hashing

        if state_key in explored:
            continue

        expanded_node_queue = expand_node(node)
        for child in expanded_node_queue:
            if EightPuzzle.is_goal(child.state):
                print_path(child)
                print(f"Length: {child.cost}")
                print(f"Expanded: {expanded_count + 1}")
                return

        explored.add(state_key)
        queue.extend(expanded_node_queue)
        expanded_count += 1
