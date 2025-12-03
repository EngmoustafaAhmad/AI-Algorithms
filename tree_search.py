# tree_search.py

from collections import deque

def tree_search(initial_state, goal_test, get_successors):
    """
    Simple Tree Search Algorithm

    Parameters:
    - initial_state: the starting point
    - goal_test: function that returns True if state is a goal
    - get_successors: function that returns next possible states

    Returns:
    - The goal state if found, otherwise None
    """

    # Frontier = list of states to explore
    frontier = deque([initial_state])

    while frontier:
        state = frontier.popleft()  # Get next state (FIFO → BFS)

        print("Exploring:", state)  # For understanding

        # Check if this is the goal
        if goal_test(state):
            print("Goal found!")
            return state

        # Add all next states to frontier
        for next_state in get_successors(state):
            frontier.append(next_state)

    return None  # No solution found


# ----------------------------------------------------
# Example usage (very simple)
# ----------------------------------------------------
if __name__ == "__main__":
    # Example: find number 7 starting from 1
    initial = 1

    def goal_test(x):
        return x == 7

    def successors(x):
        return [x + 1, x + 2]   # simple moves

    result = tree_search(initial, goal_test, successors)

    print("Result:", result)
