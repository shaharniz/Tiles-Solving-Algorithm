import numpy as np
from enum import Enum

class Directions(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

class EightPuzzle:

    _target_state = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

    def __init__(self):
        pass
   
    @staticmethod
    def validate_state_solvability(state):
        """Check if a state is 3x3 and solvable."""

        # Validate type and shape
        if not isinstance(state, np.ndarray):
            raise TypeError("State must be a NumPy array")
        if state.ndim != 2:
            raise ValueError("State must have 2 dimension")
        rows, cols = state.shape
        if rows != cols or rows != 3:
            raise ValueError("State must be 3x3 grid")
        
        # Validate solvability
        if not EightPuzzle.count_inversions(state) % 2 == 0:
            raise ValueError("State is not solvable")

    @staticmethod
    def count_inversions(state):
        """Count inversions in the puzzle state.""" 
        flat = state.flatten()
        # Remove the empty tile
        flat = [x for x in flat if x != 0]
        inversions = 0
        for i in range(len(flat)):
            for j in range(i+1, len(flat)):
                if flat[i] > flat[j]:
                    inversions += 1

        return inversions

    @staticmethod
    def get_possible_actions(state):
        possible_actions = set()
        row, col = np.argwhere(state == 0)[0]
        
        for direction in Directions:
            dr, dc = direction.value
            nr, nc = row + dr, col + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                possible_actions.add(direction)

        return possible_actions
    
    @staticmethod
    def transition(state, action):
        if action not in EightPuzzle.get_possible_actions(state):
            raise ValueError(f"Action <{action}> of type {type(action)} is not valid for current state: {state}")
        
        row, col = np.argwhere(state == 0)[0]
        dr, dc = action.value
        nr, nc = row + dr, col + dc

        new_state = state.copy()
        new_state[row, col], new_state[nr, nc] = new_state[nr, nc], new_state[row, col]
        
        return new_state

    @staticmethod
    def get_successors(state):
        successors = []

        for action in EightPuzzle.get_possible_actions(state):
            new_state = EightPuzzle.transition(state, action)
            successors.append((action, new_state))

        return successors
    
    @staticmethod
    def is_goal(state):
        return np.array_equal(EightPuzzle._target_state, state)

