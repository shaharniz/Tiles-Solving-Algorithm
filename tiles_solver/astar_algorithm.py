from .eight_puzzle import State, is_goal, linear_conflicts_heuristic, validate_state_solvability
from .search_utils import Node, SearchResult, build_path, expand_node
import heapq


def astar(initial_state: State, validate: bool = True) -> SearchResult:
    if validate:
        validate_state_solvability(initial_state)

    if is_goal(initial_state):
        return SearchResult(algorithm="A*", path=[], length=0, expanded=0)

    # Priority queue with tuples (f_cost, tie_breaker, node)
    # counter is a unique id for each tuple and acts as a tie_breaker to avoid comparison of Node objects when f_costs are equal
    counter = 0
    root = Node(state=initial_state)
    h_root = linear_conflicts_heuristic(root.state)
    f_root = root.cost + h_root

    queue = [(f_root, counter, root)]
    explored: set[bytes] = set()
    best_costs: dict[bytes, int] = {root.state.tobytes(): 0}
    expanded_count = 0

    while queue:
        # Pop the node with the lowest f_cost
        _, _, node = heapq.heappop(queue)
        state_key = node.state.tobytes()  # Converting to bytes for hashing

        # Lazy deletion: skip stale entries and states we've already expanded.
        if node.cost > best_costs.get(state_key, float("inf")) or state_key in explored:
            continue

        if is_goal(node.state):
            return SearchResult(
                algorithm="A*",
                path=build_path(node),
                length=node.cost,
                expanded=expanded_count,
            )

        expanded_node_queue = expand_node(node)
        for child in expanded_node_queue:
            child_key = child.state.tobytes()
            if child_key in explored:
                continue
            if child.cost >= best_costs.get(child_key, float("inf")):
                continue

            best_costs[child_key] = child.cost
            h_cost = linear_conflicts_heuristic(child.state)
            f_cost = child.cost + h_cost
            counter += 1
            heapq.heappush(queue, (f_cost, counter, child))

        explored.add(state_key)
        expanded_count += 1

    raise RuntimeError("A* exhausted the search frontier without reaching a goal")
