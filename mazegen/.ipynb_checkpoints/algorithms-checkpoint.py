import random
from .grid import Cell


class Solution:
    def __init__(self, sol_coord: tuple[int, int]):
        self.sol_coord = sol_coord
        self.sol_path: list[str] = []

    def get_path(self) -> str:
        return "".join(self.sol_path)


def create_path(
        maze: list[list[Cell]],
        chosen_path: str,
        pos: tuple[int, int]) -> tuple[int, int]:
    x, y = pos
    if chosen_path == "N":
        next_pos = (x, y - 1)
        maze[y][x].north = False
        maze[y - 1][x].south = False
    elif chosen_path == "E":
        next_pos = (x + 1, y)
        maze[y][x].east = False
        maze[y][x + 1].west = False
    elif chosen_path == "S":
        next_pos = (x, y + 1)
        maze[y][x].south = False
        maze[y + 1][x].north = False
    elif chosen_path == "W":
        next_pos = (x - 1, y)
        maze[y][x].west = False
        maze[y][x - 1].east = False
    return next_pos


def check_open(maze: list[list[Cell]], pos: tuple[int, int]) -> list[str]:
    open_paths = []
    x, y = pos
    if not maze[y - 1][x].visited:
        open_paths.append("N")
    if not maze[y][x + 1].visited:
        open_paths.append("E")
    if not maze[y + 1][x].visited:
        open_paths.append("S")
    if not maze[y][x - 1].visited:
        open_paths.append("W")
    return open_paths


def dfs(
        maze: list[list[Cell]],
        pos: tuple[int, int],
        solution: Solution,
        curent_path: list[str]) -> None:
    x, y = pos
    maze[y][x].visited = True
    open_paths = check_open(maze, pos)
    if pos == solution.sol_coord:
        solution.sol_path = curent_path
    while open_paths:
        next_path = random.choice(open_paths)
        next_pos = create_path(maze, next_path, pos)
        dfs(maze, next_pos, solution, curent_path + [next_path])
        open_paths = check_open(maze, pos)


def dfs_imp(
        maze: list[list[Cell]],
        pos: tuple[int, int],
        solution: Solution,
        curent_path: list[str]) -> None:
    x, y = pos
    maze[y][x].visited = True
    open_paths = check_open(maze, pos)
    if pos == solution.sol_coord:
        solution.sol_path = curent_path
    while open_paths:
        next_path = random.choice(open_paths)
        next_path2 = random.choice(open_paths)
        if next_path2 != next_path:
            create_path(maze, next_path2, pos)
        next_pos = create_path(maze, next_path, pos)
        dfs_imp(maze, next_pos, solution, curent_path + [next_path])
        open_paths = check_open(maze, pos)
