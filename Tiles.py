import sys
import numpy as np
from eight_puzzle import EightPuzzle
from bfs_algorithm import bfs
from astar_algorithm import astar


def main(argv):
    try:
        numbers = list(map(int, argv[1:]))
        if len(argv) != 10 or set(numbers) != set(range(9)):
            raise ValueError
    except ValueError:
        raise ValueError("Expected 9 arguments that must contain each integers from 0 to 8 exactly once.")

    initial_state = np.array(numbers, dtype=np.uint8).reshape(3, 3)
    EightPuzzle.validate_state_solvability(initial_state)

    print()
    bfs(initial_state)
    print()
    astar(initial_state)
    print()

    
if __name__ == "__main__":
    main(sys.argv)