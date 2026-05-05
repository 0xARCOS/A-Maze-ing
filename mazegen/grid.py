class Cell():
    def __init__(
            self,
            north: bool,
            east: bool,
            south: bool,
            west: bool,
            visited: bool) -> None:
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.visited = visited

    def get_hex(self) -> int:
        walls = [self.west, self.south, self.east, self.north]
        bits = ["1" if wall else "0" for wall in walls]
        return int("".join(bits), 2)


def grid_bound(width: int, height: int) -> list[list[Cell]]:
    maze = [[Cell(True, True, True, True, False)
            for _ in range(width + 2)]
            for _ in range(height + 2)]
    for row in maze:
        row[0].visited = True
        row[-1].visited = True
    for cell in maze[0]:
        cell.visited = True
    for cell in maze[-1]:
        cell.visited = True
    return maze


def add_42(maze: list[list[Cell]], width: int, height: int) -> None:
    x = int(width / 2)
    y = int(height / 2)
    for i in range(1, 4):
        maze[y - 2][x + i].visited = True
        maze[y + 2][x + i].visited = True
        maze[y][x + i].visited = True
        maze[y][x - i].visited = True
    maze[y - 1][x - 3].visited = True
    maze[y - 1][x + 3].visited = True
    maze[y - 2][x - 3].visited = True
    maze[y + 1][x - 1].visited = True
    maze[y + 1][x + 1].visited = True
    maze[y + 2][x - 1].visited = True


def clear_bounds(maze: list[list[Cell]]) -> None:
    del maze[0]
    del maze[-1]
    for row in maze:
        del row[0]
        del row[-1]
