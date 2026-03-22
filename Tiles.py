"""
Tiles.py - 8-Puzzle Solver Entry Point

This program accepts an initial state of the 8-puzzle as command-line arguments,
validates and solves it using BFS and A* algorithms (if solvable).
"""
import sys
import numpy as np
from eight_puzzle import EightPuzzle
from bfs_algorithm import bfs
from astar_algorithm import astar
from search_utils import print_result


def main(argv):
    try:
        numbers = list(map(int, argv[1:]))
        if len(argv) != 10 or set(numbers) != set(range(9)):
            raise ValueError
    except ValueError:
        raise ValueError("Expected 9 arguments that must contain each integers from 0 to 8 exactly once.")

    initial_state = np.array(numbers, dtype=np.uint8).reshape(3, 3)
    EightPuzzle.validate_state_solvability(initial_state)

    print_result(bfs(initial_state, validate=False))
    print_result(astar(initial_state, validate=False))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        print("\nUsage: python Tiles.py <tile_0> <tile_1> ... <tile_8>", file=sys.stderr)
        print("Example: python Tiles.py 1 4 0 5 8 2 3 6 7", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Internal search error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)
