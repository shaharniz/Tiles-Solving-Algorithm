from collections import deque

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

def bfs(puzzle):
    root = Node(puzzle.state)
    queue = deque([root])
    path = set()

    while queue:
        node = queue.popleft()

        if node.is_goal(node.state):
            return node

        path.add(node.state)

        for action, next_state in puzzle.get_successors(node.state):
            if next_state not in path:
                child = Node(
                    state=next_state,
                    parent=node,
                    action=action,
                    cost=node.cost + 1
                )
                queue.append(child)

    return None  # no solution

def astar():
    pass