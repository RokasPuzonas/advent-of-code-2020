from typing import Iterable

STEP_LOOKUP = {
    "e":  ( 1,  0),
    "w":  (-1,  0),
    "ne": ( 1,  1),
    "sw": (-1, -1),
    "nw": ( 0,  1),
    "se": ( 0, -1),
}

def read_input(filename: str) -> list[list[str]]:
    tiles = []
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            steps = []
            i = 0
            while i < len(line):
                if line[i] == "e" or line[i] == "w":
                    steps.append(line[i])
                else:
                    steps.append(line[i:i+2])
                    i += 1
                i += 1
            tiles.append(steps)
    return tiles

def get_black_tiles(tiles: list[list[str]]) -> set[tuple[int, int]]:
    black_tiles = set()

    for steps in tiles:
        x = 0
        y = 0
        for step in steps:
            dx, dy = STEP_LOOKUP[step]
            x += dx
            y += dy
        if (x, y) in black_tiles:
            black_tiles.remove((x, y))
        else:
            black_tiles.add((x, y))

    return black_tiles

def part1(tiles: list[list[str]]) -> int:
    return len(get_black_tiles(tiles))

def get_neighbors(tile: tuple[int, int]) -> Iterable[tuple[int, int]]:
    for offset in STEP_LOOKUP.values():
        neighbor = (tile[0]+offset[0], tile[1]+offset[1])
        yield neighbor

def count_neighbors(tiles: set[tuple[int, int]], tile: tuple[int, int]) -> int:
    count = 0
    for neighbor in get_neighbors(tile):
        if neighbor in tiles:
            count += 1
    return count

def simulate(black_tiles: set[tuple[int, int]]) -> set[tuple[int, int]]:
    white_tiles = set()
    for tile in black_tiles:
        for neighbor in get_neighbors(tile):
            if neighbor not in black_tiles:
                white_tiles.add(neighbor)

    new_black_tiles = set()
    # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    for black_tile in black_tiles:
        black_count = count_neighbors(black_tiles, black_tile)
        if black_count == 1 or black_count == 2:
            new_black_tiles.add(black_tile)

    # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
    for white_tile in white_tiles:
        if count_neighbors(black_tiles, white_tile) == 2:
            new_black_tiles.add(white_tile)

    return new_black_tiles

def part2(tiles: list[list[str]]) -> int:
    black_tiles = get_black_tiles(tiles)
    for _ in range(100):
        black_tiles = simulate(black_tiles)
    return len(black_tiles)

if __name__ == "__main__":
    tiles = read_input("input.txt")
    print("part1: ", part1(tiles))
    print("part2: ", part2(tiles))
