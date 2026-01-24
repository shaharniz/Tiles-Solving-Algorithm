from eight_puzzle import EightPuzzle
from search_utils import Node, print_path, expand_node
import heapq


def astar(initial_state):
    print("Algorithm: A*")
    EightPuzzle.validate_state_solvability(initial_state)

    if EightPuzzle.is_goal(initial_state):
        print("Path: ")
        print("Length: 0")
        print("Expanded: 0")
        return

    # Priority queue with tuples (f_cost, tie_breaker, node)
    # counter is a unique id for each tuple and acts as a tie_breaker to avoid comparison of Node objects when f_costs are equal
    counter = 0
    root = Node(state=initial_state)
    h_root = EightPuzzle.linear_conflicts_heuristic(root.state)
    f_root = root.cost + h_root

    queue = [(f_root, counter, root)]
    explored = set()
    expanded_count = 0

    while queue:
        # Pop the node with the lowest f_cost
        _, _, node = heapq.heappop(queue)
        state_key = node.state.tobytes()  # Converting to bytes for hashing

        # Lazy deletion: check if we've already processed this state with a lower cost (since we push duplicates to the heap instead of updating priorities),
        if state_key in explored:
            continue

        if EightPuzzle.is_goal(node.state):
            print_path(node)
            print(f"Length: {node.cost}")
            print(f"Expanded: {expanded_count}")
            return

        expanded_node_queue = expand_node(node)
        for child in expanded_node_queue:
            child_key = child.state.tobytes()
            if child_key in explored:
                continue

            h_cost = EightPuzzle.linear_conflicts_heuristic(child.state)
            f_cost = child.cost + h_cost
            counter += 1
            heapq.heappush(queue, (f_cost, counter, child))

        explored.add(state_key)
        expanded_count += 1
