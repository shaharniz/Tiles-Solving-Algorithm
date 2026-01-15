import numpy as np

class EightPuzzle:

    target_state = np.array([[0, 1, 2],
                             [3, 4, 5],
                             [6, 7, 8]])
    _total_cost = 0

    def __init__(self, initial_state):
        self.state = initial_state
        self._validate_initial_state()
   
    def _validate_initial_state(self):
        """Check if a state is 3x3 and solvable."""
        state = self.state

        # Validate type and shape
        if not isinstance(state, np.ndarray):
            raise TypeError("Initial state must be a NumPy array")
        if state.ndim != 2:
            raise ValueError("Initial state must have one 2 dimension")
        rows, cols = state.shape
        if rows != cols or rows != 3:
            raise ValueError("Initial state must be 3x3 grid")
        
        # Validate solvability
        if not self.count_inversions() % 2 == 0:
            raise ValueError("State is not solvable")

    def count_inversions(self):
        """Count inversions in the puzzle state.""" 
        flat = self.state.flatten()
        # Remove the empty tile
        flat = [x for x in flat if x != 0]
        inversions = 0
        for i in range(len(flat)):
            for j in range(i+1, len(flat)):
                if flat[i] > flat[j]:
                    inversions += 1

        return inversions

    def get_possible_actions(self):
        pass

    def transition(self, state, action):
        # TODO
        self.total_cost += 1

    def cost_function(self, state, action):
        pass

    @property
    def total_cost(self):
        return self._total_cost