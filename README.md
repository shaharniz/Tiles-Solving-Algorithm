# Tiles Solving Algorithm (8-Puzzle)

[![Tests](https://github.com/shaharniz/Tiles-Solving-Algorithm/actions/workflows/tests.yml/badge.svg)](https://github.com/shaharniz/Tiles-Solving-Algorithm/actions/workflows/tests.yml)

This project is a Python implementation of the classic 8-puzzle solved with two state-space search strategies:
- Breadth-First Search as an uninformed baseline
- A* with a linear conflicts heuristic as the informed search strategy

The repository is structured as a small installable package with:
- a reusable solver package in `tiles_solver/`
- an assignment-compatible CLI entrypoint in `Tiles.py`
- automated tests in `tests/`
- a benchmark module for comparing BFS and A*

It started as an Open University assignment for "Introduction to Artificial Intelligence" (Assignment 11), but the codebase has been refactored into a cleaner package-style project.

## Benchmark Snapshot
The current benchmark highlights the practical difference between uninformed and heuristic search on the same problem set:

| State | Solution Length | BFS Expanded | A* Expanded | BFS Time (ms) | A* Time (ms) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Basic | 2 | 2 | 2 | 0.898 | 0.120 |
| Easy | 7 | 69 | 9 | 1.307 | 0.282 |
| Medium | 14 | 1851 | 34 | 31.236 | 0.860 |
| Hard | 27 | 170471 | 2372 | 3197.992 | 64.369 |

The benchmark can be reproduced with:

```bash
python -m tiles_solver.benchmark
```

## Assignment Summary
The assignment was to implement a modular Python program named `Tiles.py` that solves the 8-puzzle as a state-space search problem.

Required parts:
- define the full problem formulation: state space, initial state, target state, actions, transition model, and cost function
- represent states efficiently, with `numpy.ndarray` and `dtype=np.uint8` recommended
- implement `BFS` as the uninformed search algorithm
- implement `A*` as the informed search algorithm
- use a heuristic stronger than the basic heuristics presented in the course book
- read the initial board from the command line as 9 values, with `0` representing the blank tile
- print for each algorithm only:
  - algorithm name
  - path found
  - solution length
  - number of expanded nodes
- implement `Expand(Node)` separately so it can be shared by both algorithms
- include a `README` explaining the design, representation, heuristic, and optimality properties

The assignment also specified:
- the target state is `[[0, 1, 2], [3, 4, 5], [6, 7, 8]]`
- uninformed successor order should be `Left, Right, Up, Down`
- the heuristic should remain admissible and consistent
- BFS should be used as the baseline for comparing solution length and search effort

## Setup
Requirements:
- Python 3.x
- NumPy

Install dependencies:

```bash
pip install -e .
```

## Running The Program
Run the package CLI with 9 integers in row-major order. `0` represents the blank tile.

```bash
python -m tiles_solver <tile_0> <tile_1> ... <tile_8>
```

Example:

```bash
python -m tiles_solver 1 4 0 5 8 2 3 6 7
```

Sample output:

```text
Algorithm: BFS
Path: 2 8 5 3 6 7 8 5 4 1
Length: 10
Expanded: 357
Algorithm: A*
Path: 2 8 5 3 6 7 8 5 4 1
Length: 10
Expanded: 10
```

## Running Tests
```bash
python -m unittest discover -s tests
```

## Development
The repository keeps the original assignment entrypoint in `Tiles.py`, but the package can also be used through the installed console script:

```bash
tiles-solver 1 4 0 5 8 2 3 6 7
```

Project metadata is configured in `pyproject.toml`, and the repository includes a GitHub Actions workflow that runs the test suite on every push and pull request. The workflow is defined in `.github/workflows/tests.yml` and currently installs the package in editable mode before running the full unittest suite.

## 1. General Program Description
The program is modular and split into problem definition, shared search utilities, search algorithms, and tests.

Main files:
- `Tiles.py`: command-line entry point. Parses the initial state, validates it, runs BFS and A*, and prints results in the assignment format.
- `tiles_solver/benchmark.py`: simple benchmark/demo script for comparing BFS and A* on sample states.
- `tiles_solver/eight_puzzle.py`: defines the 8-puzzle problem, including the target state, successor generation, inversion counting, solvability validation, and the heuristic.
- `tiles_solver/search_utils.py`: shared search helpers such as the `Node` class, path reconstruction, result printing, and node expansion.
- `tiles_solver/bfs_algorithm.py`: Breadth-First Search implementation.
- `tiles_solver/astar_algorithm.py`: A* implementation.
- `tests/`: unit tests for algorithms, utilities, and puzzle logic.

Internally, both `bfs()` and `astar()` return a structured result object containing the algorithm name, path, solution length, and expanded node count. The CLI layer is responsible for printing that result. This keeps the search logic separate from presentation and makes the code easier to test.

## 2. Problem Representation
### State Representation
Each state is represented as a `numpy.ndarray` of shape `(3, 3)` with `dtype=np.uint8`. This is compact, easy to copy when generating successors, and efficient to hash via `state.tobytes()` for reached/explored sets.

### Transition Model
The initial state is read from the command line and reshaped into a 3x3 array. Successors are generated by swapping the blank tile with a valid adjacent tile. The program copies the current state, applies the swap, and records the moved tile as the step label so the final path can be printed as a sequence of tile numbers.

### Cost Function
Each move has unit cost, so the path cost is the number of moves taken from the start state.

## 3. Heuristic
The A* implementation uses the linear conflicts heuristic:

`h(n) = ManhattanDistance(n) + 2 * LinearConflicts(n)`

The heuristic improves on plain Manhattan distance by detecting cases where two tiles are in their correct row or column but are reversed relative to their goal order. Each such conflict requires at least two extra moves beyond the Manhattan estimate, so each conflict contributes `2`.

For the assignment's sample initial state:

```text
[[1, 4, 0],
 [5, 8, 2],
 [3, 6, 7]]
```

the heuristic value is `10`.

Admissibility:
- Manhattan distance is admissible.
- Linear conflict adds only mandatory extra moves, so the combined heuristic remains admissible.

Consistency:
- Manhattan distance is consistent.
- Linear conflict is also consistent for the 8-puzzle, so the combined heuristic is consistent.
- Therefore the A* implementation remains optimal with this heuristic.

## 4. Algorithm Optimality
### BFS
BFS is optimal in this problem because every action has the same cost (`1`). Therefore, the first solution found is guaranteed to have the minimum number of moves.

The downside is efficiency: BFS expands many more nodes and uses much more memory than A*.

### A*
A* is optimal here because it uses an admissible and consistent heuristic. It finds a shortest solution while typically expanding far fewer nodes than BFS.

The implementation also keeps a `best_costs` dictionary for discovered states. This stores the cheapest path cost `g(n)` found so far for each state and prevents pushing a worse duplicate of the same state into the priority queue. That does not change correctness for this problem, but it reduces unnecessary heap entries and makes the search more efficient.
