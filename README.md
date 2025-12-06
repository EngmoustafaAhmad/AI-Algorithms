# 1. Tree Search
## A fundamental AI method for exploring possible paths to reach a goal

Key Concepts

Expands nodes one by one

Can follow different strategies (BFS, DFS)

Stops when the goal is found

Builds a search tree (different from state space)

Use Cases

Pathfinding

Planning

Game move exploration

# 2. Backtracking
## A depth-based technique that builds solutions step-by-step and undoes invalid moves

Key Concepts

Recursive exploration

Tries different choices

Backtracks when reaching a dead end

Use Cases

N-Queens

Sudoku

Maze solving

Constraint satisfaction

# 3. Heuristic Search (Best-First Search)
## A heuristic-guided search that explores the most promising states first

Key Concepts

Uses heuristic function h(n)

Selects the most promising node

Faster than uninformed search

May not be fully optimal

Use Cases

GPS routing

Game AI

Large search problems

# 4. Forward Chaining
## A data-driven reasoning method that starts from known facts and derives new ones

Key Concepts

Starts with existing facts

Applies all valid rules

Continues until no new facts or goal reached

Use Cases

Expert systems

Decision automation

Diagnostics

# 5. Backward Chaining
## A goal-driven reasoning method that works backward from the goal to needed facts

Key Concepts

Starts from goal

Looks for rules that satisfy the goal

Recursively checks rule conditions

Use Cases

Logic reasoning

Prolog inference

Expert systems
