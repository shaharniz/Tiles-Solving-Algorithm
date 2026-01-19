import numpy as np
from enum import Enum


class Actions(Enum):
    # (row, col)
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


class EightPuzzle:
    """
    Stateless definition of the 8puzzle problem.
    Provides goal test, successor generation, and state validation.
    """

    _target_state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.uint8)

    @staticmethod
    def validate_state_solvability(state):
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
            raise ValueError(
                "State must only contain each digit from 0 to 8 exactly once"
            )

        # Validate solvability
        if EightPuzzle.count_inversions(state) % 2 != 0:
            raise ValueError("State is not solvable")

        return True

    @staticmethod
    def count_inversions(state):
        """
        Count inversions in the puzzle state, assuming state is valid.
        """
        flat = state.flatten()
        # Remove the empty tile
        flat = [x for x in flat if x != 0]
        inversions = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if flat[i] > flat[j]:
                    inversions += 1

        return inversions

    @staticmethod
    def get_successors(state):
        successors = {}

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

                successors[action] = new_state

        return successors

    @staticmethod
    def is_goal(state):
        return np.array_equal(EightPuzzle._target_state, state)
