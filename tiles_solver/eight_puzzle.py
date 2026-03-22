from __future__ import annotations

import numpy as np
from enum import Enum
from numpy.typing import NDArray


class Actions(Enum):
    # (row, col)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)


State = NDArray[np.uint8]
TARGET_STATE: State = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)
TARGET_STATE.flags.writeable = False


def validate_state_solvability(state: State) -> bool:
    """Check if a state is 3x3 and solvable."""

    # Validate type, subtype and shape
    if not isinstance(state, np.ndarray):
        raise TypeError("State must be a NumPy array")
    if state.ndim != 2:
        raise ValueError("State must have 2 dimension")
    rows, cols = state.shape
    if rows != cols or rows != 3:
        raise ValueError("State must be 3x3 grid")
    if state.dtype != np.uint8:
        raise TypeError("State must contain only uint8 values")
    if set(state.flatten()) != set(range(9)):
        raise ValueError("State must only contain each digit from 0 to 8 exactly once")

    # Validate solvability
    if count_inversions(state) % 2 != 0:
        raise ValueError("State is not solvable")

    return True


def count_inversions(state: State) -> int:
    """
    Count inversions in the puzzle state, assuming state is valid.
    """
    flat = state.flatten()
    # Remove the empty tile
    flat = [x for x in flat if x != 0]
    inversions = 0
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1

    return inversions


def _get_action_as_step(prev_state: State, new_state: State) -> str:
    diff = prev_state.astype(np.int8) - new_state.astype(np.int8)
    positive_nonzero = np.max(diff)

    return str(positive_nonzero)


def _count_conflicts(line: list[int]) -> int:
    if not line:
        return 0

    n = len(line)

    # Calculating Longest Increasing Subsequence (LIS) length
    # Initializing dp, so that dp[i] will represent the length of LIS ending at index i
    dp = [1] * n
    for curr in range(1, n):
        for prev in range(curr):
            if line[prev] < line[curr]:
                dp[curr] = max(dp[curr], dp[prev] + 1)

    lis_length = max(dp)
    return n - lis_length


def get_successors(state: State) -> dict[str, State]:
    successors: dict[str, State] = {}

    row, col = np.argwhere(state == 0)[0]

    for action in Actions:
        dr, dc = action.value
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            # The current direction is a valid action for this state.
            new_state = state.copy()
            new_state[row, col], new_state[nr, nc] = (
                new_state[nr, nc],
                new_state[row, col],
            )

            step = _get_action_as_step(state, new_state)
            successors[step] = new_state

    return successors


def is_goal(state: State) -> bool:
    return np.array_equal(TARGET_STATE, state)


def linear_conflicts_heuristic(state: State) -> int:
    """
    The idea is to calculate the Manhattan distance and add 2 times the number of linear conflicts.
    A linear conflict occurs when two tiles are in their goal row or column but are reversed relative to their goal positions.
    The linear conflicts are multiplied by 2 because each conflict will require at least two moves, additional to the Manhattan distance, to solve the puzzle (moving away from the current row/col to resolve the reversed positions and returning back).
    Both row and column conflicts are considered because they are independent (if a tile is in its goal row and column then there's no conflict).
    """
    manhattan_distance = 0
    linear_conflicts = 0

    # Calculating Manhattan distance and row linear conflicts
    for row in range(3):
        row_candidates = []

        for col in range(3):
            tile = int(state[row, col])
            if tile == 0:
                continue

            target_row, target_col = divmod(tile, 3)
            manhattan_distance += abs(target_row - row) + abs(target_col - col)

            if tile // 3 == row:
                row_candidates.append(tile)

        linear_conflicts += _count_conflicts(row_candidates)

    # Calculating column linear conflicts
    for col in range(3):
        col_candidates = []

        for row in range(3):
            tile = int(state[row, col])
            if tile == 0:
                continue

            if tile % 3 == col:
                col_candidates.append(tile)

        linear_conflicts += _count_conflicts(col_candidates)

    return manhattan_distance + 2 * linear_conflicts
