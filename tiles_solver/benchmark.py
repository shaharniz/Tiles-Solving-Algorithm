from __future__ import annotations

from collections.abc import Callable
from time import perf_counter

import numpy as np

from .astar_algorithm import astar
from .bfs_algorithm import bfs
from .eight_puzzle import State
from .search_utils import SearchResult


SAMPLE_STATES: list[tuple[str, State]] = [
    ("basic", np.array([[1, 2, 0], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)),
    ("easy", np.array([[1, 4, 2], [7, 5, 0], [3, 6, 8]], dtype=np.uint8)),
    ("medium", np.array([[5, 4, 0],[2, 1, 3],[6, 7, 8]], dtype=np.uint8)),
    ("hard", np.array([[8, 6, 7], [2, 5, 4], [3, 0, 1]], dtype=np.uint8)),
]


def benchmark_solver(
    name: str, solver: Callable[[State], SearchResult], state: State
) -> dict[str, int | float | str]:
    start = perf_counter()
    result = solver(state)
    duration_ms = (perf_counter() - start) * 1000
    return {
        "solver": name,
        "length": result.length,
        "expanded": result.expanded,
        "time_ms": round(duration_ms, 3),
    }


def main() -> None:
    print("\n8-puzzle benchmark")
    for label, state in SAMPLE_STATES:
        print(f"\nState: {label}")
        print(state)
        bfs_metrics = benchmark_solver("BFS", bfs, state)
        astar_metrics = benchmark_solver("A*", astar, state)
        print(
            f"{bfs_metrics['solver']}: length={bfs_metrics['length']}, "
            f"expanded={bfs_metrics['expanded']}, time_ms={bfs_metrics['time_ms']}"
        )
        print(
            f"{astar_metrics['solver']}: length={astar_metrics['length']}, "
            f"expanded={astar_metrics['expanded']}, time_ms={astar_metrics['time_ms']}"
        )


if __name__ == "__main__":
    main()
