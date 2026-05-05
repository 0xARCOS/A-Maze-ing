import random
from collections import deque
from .algorithms import dfs, dfs_imp, Solution
from .grid import grid_bound, add_42, clear_bounds, Cell


def create_file(
        maze: list[list[Cell]],
        start_p: tuple[int, int],
        finish_p: tuple[int, int],
        solution_path: str,
        name: str) -> None:
    s_x, s_y = start_p
    f_x, f_y = finish_p
    with open(name, "w") as file:
        for row in maze:
            file.write("".join(f"{cell.get_hex():X}" for cell in row))
            file.write("\n")
        file.write("\n")
        file.write(f"{s_x},{s_y}\n")
        file.write(f"{f_x},{f_y}\n")
        file.write(solution_path)


def find_solution(
        maze: list[list[Cell]],
        solution: Solution,
        start_p: tuple[int, int]) -> None:
    target = solution.sol_coord
    queue: deque[tuple[tuple[int, int], list[str]]] = deque([(start_p, [])])
    visited = {start_p}
    directions = ["N", "E", "S", "W"]
    while queue:
        pos, path = queue.popleft()
        if pos == target:
            solution.sol_path = path
            return
        x, y = pos
        cell = maze[y][x]
        for dir in directions:
            if dir == "N" and not cell.north:
                next_pos = (x, y - 1)
            elif dir == "E" and not cell.east:
                next_pos = (x + 1, y)
            elif dir == "S" and not cell.south:
                next_pos = (x, y + 1)
            elif dir == "W" and not cell.west:
                next_pos = (x - 1, y)
            else:
                continue
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, path + [dir]))


def close_big_spaces(maze: list[list[Cell]]) -> None:
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if (
                not any([cell.north, cell.east, cell.south, cell.west])
                and
                not any([maze[y + 1][x].east, maze[y + 1][x].west])
                and
                not any([maze[y - 1][x].east, maze[y - 1][x].west])
                and
                not any([maze[y][x + 1].north, maze[y][x + 1].south])
                and
                not any([maze[y][x - 1].north, maze[y][x - 1].south])
            ):
                cell.south = True
   

class MazeGenerator:
    def generate_perfect(
            self,
            width: int,
            height: int,
            entry: tuple[int, int],
            exit: tuple[int, int],
            name: str,
            perfect: bool,
            seed: int | None) -> None:
        """Generates the perfect maze"""
        if seed:
            random.seed(seed)
        maze: list[list[Cell]] = grid_bound(width, height)
        if width >= 7 and height >= 5:
            add_42(maze, width + 2, height + 2)
        else:
            print("Couldnt print 42, not enought space")
        start_p = (entry[0] + 1, entry[1] + 1)
        finish_p = (exit[0] + 1, exit[1] + 1)
        if (
            maze[start_p[1]][start_p[0]].visited
            or
            maze[finish_p[1]][finish_p[0]].visited
        ):
            raise ValueError("Entry or exit, inside '42' pattern")
        solution = Solution(finish_p)
        current_path: list[str] = []
        if not perfect:
            dfs_imp(maze, start_p, solution, current_path)
            close_big_spaces(maze)
            find_solution(maze, solution, start_p)
        else:
            dfs(maze, start_p, solution, current_path)
        clear_bounds(maze)
        create_file(maze, entry, exit, solution.get_path(), name)
