from __future__ import annotations

from dataclasses import dataclass

from .eight_puzzle import State, get_successors


@dataclass(slots=True)
class Node:
    state: State
    parent: Node | None = None
    step: str | None = None
    cost: int = 0


@dataclass(frozen=True, slots=True)
class SearchResult:
    algorithm: str
    path: list[str]
    length: int
    expanded: int


def build_path(node: Node) -> list[str]:
    path: list[str] = []
    current: Node | None = node
    while current is not None:
        if current.step is not None:
            path.append(current.step)
        current = current.parent
    return list(reversed(path))


def print_result(result: SearchResult) -> None:
    print(f"Algorithm: {result.algorithm}")
    print("Path:", " ".join(result.path))
    print(f"Length: {result.length}")
    print(f"Expanded: {result.expanded}")


def expand_node(node: Node) -> list[Node]:
    expanded_nodes: list[Node] = []
    for step, next_state in get_successors(node.state).items():
        child = Node(
            state=next_state,
            parent=node,
            step=step,
            cost=node.cost + 1,
        )
        expanded_nodes.append(child)

    return expanded_nodes
