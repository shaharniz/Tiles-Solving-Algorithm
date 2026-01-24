# Tiles Solving Algorithm (8-Puzzle)

This project implements a solver for the 8-puzzle problem using search algorithms as part of the "Introduction to Artificial Intelligence" course (Assignment 11).

## Algorithms
The solver utilizes two search strategies:
1.  **Breadth-First Search (BFS)**: An uninformed search algorithm.
2.  **A\* Search**: An informed search algorithm using the **Linear Conflicts Heuristic** (Manhattan Distance + 2 * Linear Conflicts) to efficiently find the optimal solution.

## Prerequisites
*   Python 3.x
*   NumPy

```bash
pip install numpy
```

## Usage
Run the `Tiles.py` script with 9 distinct integers (0-8) representing the initial state of the 3x3 grid (row-major order). `0` represents the empty tile.

```bash
python Tiles.py <tile_0> <tile_1> ... <tile_8>
```

### Example
```bash
python Tiles.py 1 4 0 5 8 2 3 6 7
```

## Running Tests
Unit tests are provided to verify the puzzle logic and heuristics.

```bash
python -m unittest discover
```

---

## Problem Definition

### State Space
All possible arrangements of a 3x3 grid (numpy array) containing "tiles" (cells) numbered from 0 to 8 that are solvable.
The total number of solvable states is 9!/2 = 181,440 because of the parity property (See course guide page 52, course book pages 86, 115).

### Target State
Tiles grid ordered as such:
```
[[0, 1, 2],
 [3, 4, 5],
 [6, 7, 8]]
```

### Actions
Moving the empty tile (`0`) in one of four directions (if allowed): **UP**, **DOWN**, **LEFT** and **RIGHT**.

An action is allowed if the empty tile is not on the edge of the grid in the direction of the move.
For an uninformed search, we will take actions in the following order: **LEFT**, **RIGHT**, **UP**, **DOWN**.

### Transition Model
Applying an action to a state results in a new state where the empty tile (`0`) has swapped places with the adjacent tile in the direction of the move (if the action is allowed).

For example, if in a state the `0` tile is at position `(1,1)` and the action **LEFT** is applied, the new state will swap it with the tile at `(1,0)`.

### Cost Function
Each action costs 1.
