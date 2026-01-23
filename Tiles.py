"""
8Puzzle 

State Space:
All possible arrangements of a 3x3 grid (numpy array) containing "tiles" (cells) numbered from 0 to 8 that are solvable.
The total number of solvable states is 9!/2 = 181,440 because of the parity property (See course guide page 52, course book pages 86, 115).

Initial State:
The initial state is provided by the user as command line arguments numbered from 0 to 8 (for example: Tiles.py 1 4 0 5 8 2 3 6 7).
If the input is valid (matches one of the state spaces), it will be represented as a 3x3 grid.
The number 0 represents the empty tile.

Target State: 
Tiles grid ordered as such -
[[0, 1, 2],
 [3, 4, 5],
 [6, 7, 8]]

Actions:
Moving the empty tile (0) in one of four directions (if allowed) - UP, DOWN, LEFT and RIGHT
An action is allowed if the empty tile is not on the edge of the grid in the direction of the move.
For an uninformed search, we will take actions in the following order: LEFT, RIGHT, UP, DOWN.

Transition Model:
Applying an action to a state results in a new state where the empty tile (0) has swapped places with the adjacent tile in the direction of the move (if the action is allowed).
For example, if in a state the 0 tile is at position (1,1) and the action LEFT is applied, the new state will swap it with the tile at (1,0).

Cost Function:
Each action costs 1.
"""
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

    bfs(initial_state)
    
    # TODO

if __name__ == "__main__":
    main(sys.argv)