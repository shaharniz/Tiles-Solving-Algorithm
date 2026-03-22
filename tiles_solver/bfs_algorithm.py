from collections import deque
from .eight_puzzle import State, is_goal, validate_state_solvability
from .search_utils import Node, SearchResult, build_path, expand_node


def bfs(initial_state: State, validate: bool = True) -> SearchResult:
    if validate:
        validate_state_solvability(initial_state)

    if is_goal(initial_state):
        return SearchResult(algorithm="BFS", path=[], length=0, expanded=0)

    root = Node(state=initial_state)
    queue = deque([root])
    frontier = {root.state.tobytes()}
    explored: set[bytes] = set()
    expanded_count = 0

    while queue:
        node = queue.popleft()
        state_key = node.state.tobytes()  # Converting to bytes for hashing
        frontier.discard(state_key)

        if state_key in explored:
            continue

        expanded_node_queue = expand_node(node)
        for child in expanded_node_queue:
            child_key = child.state.tobytes()
            if child_key in explored or child_key in frontier:
                continue

            if is_goal(child.state):
                return SearchResult(
                    algorithm="BFS",
                    path=build_path(child),
                    length=child.cost,
                    expanded=expanded_count + 1,
                )

            frontier.add(child_key)
            queue.append(child)

        explored.add(state_key)
        expanded_count += 1

    raise RuntimeError("BFS exhausted the search frontier without reaching a goal")
