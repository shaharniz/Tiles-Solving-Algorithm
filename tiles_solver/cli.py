import sys
from collections.abc import Sequence

import numpy as np

from .astar_algorithm import astar
from .bfs_algorithm import bfs
from .eight_puzzle import validate_state_solvability
from .search_utils import print_result


def main(argv: Sequence[str]) -> None:
    try:
        numbers = list(map(int, argv[1:]))
        if len(argv) != 10 or set(numbers) != set(range(9)):
            raise ValueError
    except ValueError:
        raise ValueError(
            "Expected 9 arguments that must contain each integers from 0 to 8 exactly once."
        )

    initial_state = np.array(numbers, dtype=np.uint8).reshape(3, 3)
    validate_state_solvability(initial_state)

    print_result(bfs(initial_state, validate=False))
    print_result(astar(initial_state, validate=False))


def run(argv: Sequence[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv

    try:
        main(argv)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        program = argv[0] if argv else "tiles-solver"
        print(f"\nUsage: {program} <tile_0> <tile_1> ... <tile_8>", file=sys.stderr)
        print(f"Example: {program} 1 4 0 5 8 2 3 6 7", file=sys.stderr)
        raise SystemExit(1) from None
    except RuntimeError as e:
        print(f"Internal search error: {e}", file=sys.stderr)
        raise SystemExit(1) from None
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        raise SystemExit(1) from None
