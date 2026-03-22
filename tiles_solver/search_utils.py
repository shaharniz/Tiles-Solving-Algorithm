from dataclasses import dataclass
from .eight_puzzle import get_successors


class Node:
    def __init__(self, state, parent=None, step=None, cost=0):
        self.state = state
        self.parent = parent
        self.step = step
        self.cost = cost


@dataclass(frozen=True)
class SearchResult:
    algorithm: str
    path: list[str]
    length: int
    expanded: int


def build_path(node):
    path = []
    while node:
        if node.step is not None:
            path.append(node.step)
        node = node.parent
    return list(reversed(path))


def print_result(result):
    print(f"Algorithm: {result.algorithm}")
    print("Path:", " ".join(result.path))
    print(f"Length: {result.length}")
    print(f"Expanded: {result.expanded}")


def expand_node(node):
    expanded_nodes = []
    for step, next_state in get_successors(node.state).items():
        child = Node(
            state=next_state,
            parent=node,
            step=step,
            cost=node.cost + 1,
        )
        expanded_nodes.append(child)

    return expanded_nodes
