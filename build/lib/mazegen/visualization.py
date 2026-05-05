from typing import Generator
from pathlib import Path


RESET = "\033[0m"
WHITE = "\033[37m"
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
GRAY = "\033[90m"
colors = [WHITE, RED, GREEN, CYAN, GRAY]


def color_generator() -> Generator[str, None, None]:
    while True:
        for color in colors:
            yield color

def check_lines(lines: list[str]) -> bool:
    length = len(lines[0])
    for line in lines[:-4]:
        if len(line) != length:
            return False
    return True


def convert_bits(lines: list[str]) -> list[list[str]]:
    bit_lines = []
    for line in lines:
        bits = []
        for c in line:
            bits.append(f"{int(c, 16):04b}")
        bit_lines.append(bits)
    return bit_lines


def build_grid(
        bit_lines: list[list[str]],
        entry: tuple[int, int],
        exit: tuple[int, int],
        path_positions: set[tuple[int, int]],
        show_path: bool) -> list[list[str]]:
    grid = []
    row = []
    row.append("+")
    for bits in bit_lines[0]:
        if bits[3] == "1":
            row.append("---")
        else:
            row.append("   ")
        row.append("+")
    grid.append(row)

    for y, line in enumerate(bit_lines):
        row = []
        if line[0][0] == "1":
            row.append("\n|")
        for x, bits in enumerate(line):
            if bits == "1111":
                cell = "███"
            elif (x, y) == entry:
                cell = " S "
            elif (x, y) == exit:
                cell = " F "
            elif show_path and (x, y) in path_positions:
                cell = " ◉ "
            else:
                cell = "   "
            row.append(cell)
            if bits[2] == "1":
                row.append("|")
            else:
                row.append(" ")
        grid.append(row)
        row = []
        row.append("\n+")
        for bits in line:
            if bits[1] == "1":
                row.append("---")
            else:
                row.append("   ")
            row.append("+")
        grid.append(row)
    return grid


def visualize(path: Path) -> tuple[str, str]:
    with path.open("r") as file:
        lines = file.read().splitlines()
    if not check_lines(lines):
        raise ValueError("Bad formar por map file")
    bit_lines = convert_bits(lines[:-4])
    tmp_list = lines[-3].split(",")
    entry = (int(tmp_list[0]), int(tmp_list[1]))
    tmp_list = lines[-2].split(",")
    exit = (int(tmp_list[0]), int(tmp_list[1]))
    solution_path = lines[-1]

    path_positions = set()
    curr = entry
    for move in solution_path:
        if move == "N":
            curr = (curr[0], curr[1] - 1)
        elif move == "E":
            curr = (curr[0] + 1, curr[1])
        elif move == "S":
            curr = (curr[0], curr[1] + 1)
        elif move == "W":
            curr = (curr[0] - 1, curr[1])
        path_positions.add(curr)

    grid_without = build_grid(bit_lines, entry, exit, path_positions, False)
    grid_with = build_grid(bit_lines, entry, exit, path_positions, True)
    return (
        "".join("".join(r) for r in grid_without),
        "".join("".join(r) for r in grid_with)
        )
