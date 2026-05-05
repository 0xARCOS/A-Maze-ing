*This project has been created as part of the 42 curriculum by mumehmed, ariarcos.*

# A-Maze-ing

A Python maze generator and visualization tool.

## Description

A-Maze-ing generates mazes using depth-first search (DFS) algorithms. It supports both perfect mazes (exactly one path between any two points) and imperfect mazes (with loops and multiple solutions). The tool provides interactive visualization with solution path highlighting and configurable color schemes.

The goal of this project is to create a maze generator that can produce mazes of varying sizes and complexities, with the ability to solve them and visualize the solution path in the terminal.

### Key Features

- **Maze Generation**: Create perfect or imperfect mazes using DFS algorithms
- **Interactive Visualization**: View and explore generated mazes in the terminal
- **Solution Path**: Display the solution path from entry to exit using BFS
- **Customizable Colors**: Multiple color schemes for visual variety
- **Configurable**: Flexible configuration via text files
- **Reproducible**: Optional seed support for deterministic maze generation
- **ASCII Art**: Hidden "42" pattern when maze is large enough

## Instructions

### Installation

```bash
pip install -r requirements.txt
```

Or install the package:

```bash
pip install .
```

### Running the Project

Run the maze generator with a configuration file:

```bash
python a_maze_ing.py config.txt
```

Or use the Makefile:

```bash
make run
```

### Interactive Controls

Once running, use the following commands:

- `1` - Regenerate maze
- `2` - Show/Hide solution path
- `3` - Change maze colors
- `4` - Quit

### Configuration File

Create a `config.txt` file with the following structure:

```
#Maze width (number of cells)
WIDTH=11

#Maze height
HEIGHT=11

#Entry coordinates (x,y)
ENTRY=0,0

#Exit coordinates (x,y)
EXIT=9,9

#Output filename
OUTPUT_FILE=maze.txt

#Is the maze perfect?
PERFECT=true

seed=
```

| Option | Description | Required | Default |
|--------|-------------|----------|---------|
| `WIDTH` | Number of cells horizontally (positive integer) | Yes | - |
| `HEIGHT` | Number of cells vertically (positive integer) | Yes | - |
| `ENTRY` | Entry coordinates as `x,y` (0-indexed) | Yes | - |
| `EXIT` | Exit coordinates as `x,y` (0-indexed) | Yes | - |
| `OUTPUT_FILE` | Output filename for the maze | No | `maze.txt` |
| `PERFECT` | `true` for perfect maze, `false` for imperfect | No | `true` |
| `seed` | Optional seed for reproducible mazes (integer or empty) | No | Random |

### Development Commands

Run lint checks:
```bash
make lint
```

Run strict lint checks:
```bash
make lint-strict
```

Clean temporary files:
```bash
make clean
```

## Maze Generation Algorithm

### Algorithm Used: Depth-First Search (DFS)

The project uses **Recursive Depth-First Search (DFS)** as the primary maze generation algorithm. Two variants are implemented:

1. **Perfect Maze (DFS)**: Creates a maze with exactly one path between any two points. Uses standard recursive DFS with backtracking.

2. **Imperfect Maze (DFS with random additional passages)**: Creates a maze with loops by randomly adding extra passages during the DFS traversal.

### Why DFS?

DFS was chosen for the following reasons:

1. **Simplicity**: DFS is straightforward to implement and understand
2. **Efficiency**: O(V + E) time complexity where V is vertices and E is edges
3. **Maze Quality**: DFS naturally produces long, winding corridors ideal for mazes
4. **Perfect Mazes**: DFS guarantees a perfect maze (spanning tree) when used with backtracking
5. **Low Memory**: Only requires tracking the current path, not the entire frontier like some algorithms

### Solution Finding

The solution path is found using **Breadth-First Search (BFS)**, which guarantees the shortest path in an unweighted grid.

## Code Reusability

The codebase is modular and the following components are reusable:

### `mazegen/grid.py`
- `Cell` class: Represents a single cell with wall information
- `grid_bound()`: Creates a bordered grid - reusable for any grid-based algorithm
- `clear_bounds()`: Removes border from grid - useful for other applications

### `mazegen/algorithms.py`
- `Solution` class: Tracks solution coordinates and path - reusable for pathfinding
- `check_open()`: Checks available paths from a position - reusable for navigation
- `create_path()`: Updates wall status between cells - reusable for maze modifications
- `dfs()` / `dfs_imp()`: Generic maze generation algorithms

### `mazegen/config_check.py`
- Configuration parsing and validation with Pydantic - reusable for other config-driven projects

### `mazegen/visualization.py`
- Terminal-based maze rendering - adaptable for different display formats

### `mazegen/maze_generator.py`
- `MazeGenerator` class: Main orchestration logic - adaptable for different maze types
- `find_solution()`: BFS pathfinding - reusable for any grid pathfinding task
- `close_big_spaces()`: Post-processing for imperfect mazes

## Team and Project Management

### Team Members

- **mumehmed**: Primary developer, architecture design, algorithms implementation
- **ariarcos**: Secondary developer, configuration system, visualization

### Roles

| Member | Primary Responsibilities |
|--------|-------------------------|
| mumehmed | DFS algorithm implementation, grid representation, solution finding |
| ariarcos | Configuration parsing, terminal visualization, interactive CLI |

### Planning and Execution

1. **Initial Planning**: Defined project scope - maze generation with DFS and terminal visualization
2. **Algorithm Development**: Implemented DFS for perfect mazes, then extended to imperfect mazes
3. **Configuration System**: Created config.txt parsing with Pydantic validation
4. **Visualization**: Built ASCII/Unicode-based terminal visualization
5. **Interactive Features**: Added solution path toggle and color cycling
6. **Refinement**: Added "42" easter egg for large mazes, polished user experience

### What Worked Well

- Clear separation of concerns with modular design
- Using Pydantic for configuration validation prevented runtime errors
- BFS for solution finding is reliable and fast
- Interactive CLI provides good user experience for exploration

### What Could Be Improved

- Add more maze generation algorithms (Prim's, Kruskal's, Recursive Division)
- Support graphical output (matplotlib, pygame)
- Add unit tests for better code coverage
- Implement maze difficulty rating based on solution complexity

### Tools Used

- **Python 3**: Primary language
- **Pydantic**: Configuration validation
- **flake8**: Code linting
- **mypy**: Static type checking
- **Make**: Build automation

## Resources

### References

- [Depth-First Search - Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)
- [Maze Generation Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Breadth-First Search - Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Pydantic Documentation](https://docs.pydantic.dev/)

### AI Usage

AI was used for:
- Code review and suggested improvements
- README structure and documentation guidance
- Explaining algorithmic concepts and time complexity
- General debugging assistance

AI was NOT used for:
- Writing the core DFS algorithm implementation
- Creating the grid representation
- Implementing the solution finder (BFS)
- Building the interactive CLI

All core algorithmic implementations were written by the team members.