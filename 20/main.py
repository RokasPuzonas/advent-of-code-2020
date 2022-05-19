from dataclasses import dataclass
from typing import Iterator, Optional
from math import floor

@dataclass
class Tile:
    top: str
    left: str
    right: str
    bottom: str

    inner: list[str]

    def __repr__(self) -> str:
        return "Tile"

TilesData = dict[int, Tile]
TileGrid = list[list[Optional[tuple[int, Tile]]]]

def parse_tile(tile_data: str) -> tuple[int, Tile]:
    lines = tile_data.splitlines()
    id = int(lines[0][4:-1])
    top_edge = lines[1]
    right_edge = "".join(line[-1] for line in lines[1:])
    left_edge = "".join(line[0] for line in lines[1:])
    bottom_edge = lines[-1]

    raw_inner = list(line[1:-1] for line in lines[2:-1])

    return id, Tile(top_edge, left_edge, right_edge, bottom_edge, raw_inner)

def parse_input(filename: str) -> TilesData:
    tiles = {}
    with open(filename, "r") as f:
        content = f.read()
        for block in content.split("\n\n"):
            id, tile = parse_tile(block)
            tiles[id] = tile
    return tiles

def flip_image(image: list[str]):
    return image[::-1]

def rotate_image(image: list[str]):
    return ["".join(col[::-1]) for col in zip(*image)]

def rotate_tile(tile) -> Tile:
    return Tile(
        top = tile.left[::-1],
        right = tile.top,
        bottom = tile.right[::-1],
        left = tile.bottom,

        inner=rotate_image(tile.inner)
    )

def flip_tile(tile) -> Tile:
    return Tile(
        top = tile.bottom,
        right = tile.right[::-1],
        bottom = tile.top,
        left = tile.left[::-1],

        inner=tile.inner[::-1]
    )

def get_grid_size(tiles: TilesData) -> int:
    return floor(len(tiles)**0.5)

def get_rotated_tiles(tile: Tile) -> Iterator[Tile]:
    yield tile
    tile = rotate_tile(tile)
    yield tile
    tile = rotate_tile(tile)
    yield tile
    tile = rotate_tile(tile)
    yield tile

def get_tile_variants(tile: Tile) -> Iterator[Tile]:
    for t in get_rotated_tiles(tile):
        yield t

    tile = flip_tile(tile)
    for t in get_rotated_tiles(tile):
        yield t

def get_image_variants(image: list[str]) -> Iterator[list[str]]:
    yield image
    image = rotate_image(image)
    yield image
    image = rotate_image(image)
    yield image
    image = rotate_image(image)
    yield image
    image = rotate_image(image)

    image = flip_image(image)
    yield image
    image = rotate_image(image)
    yield image
    image = rotate_image(image)
    yield image
    image = rotate_image(image)
    yield image

def is_tile_possible(grid: TileGrid, x: int, y: int, tile: Tile) -> bool:
    if x > 0:
        other_tile = grid[y][x-1]
        if other_tile and other_tile[1].right != tile.left:
            return False

    if x < len(grid[0])-1:
        other_tile = grid[y][x+1]
        if other_tile and other_tile[1].left != tile.right:
            return False

    if y > 0:
        other_tile = grid[y-1][x]
        if other_tile and other_tile[1].bottom != tile.top:
            return False

    if y < len(grid)-1:
        other_tile = grid[y+1][x]
        if other_tile and other_tile[1].top != tile.bottom:
            return False

    return True

def get_possible_tiles(
        tiles_data: TilesData,
        used_tiles: list[int],
        grid: TileGrid,
        x: int,
        y: int
    ) -> Iterator[tuple[int, Tile]]:
    for id in tiles_data.keys():
        if id not in used_tiles:
            for variant in get_tile_variants(tiles_data[id]):
                if is_tile_possible(grid, x, y, variant):
                    yield id, variant

def solve(tiles_data: TilesData, grid: TileGrid, used_tiles: list[int] = []) -> bool:
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == None:
                for id, tile in get_possible_tiles(tiles_data, used_tiles, grid, x, y):
                    grid[y][x] = (id, tile)
                    used_tiles.append(id)
                    if solve(tiles_data, grid):
                        return True
                    used_tiles.pop()
                    grid[y][x] = None
                return False

    return True

def multiply_corners(grid: TileGrid) -> int:
    w = len(grid[0])
    h = len(grid)
    top_left = grid[0][0]
    top_right = grid[0][w-1]
    bottom_left = grid[h-1][0]
    bottom_right = grid[h-1][w-1]
    assert top_left
    assert top_right
    assert bottom_left
    assert bottom_right
    return top_left[0] * top_right[0] * bottom_right[0] * bottom_left[0]

def solve_grid(tiles_data: TilesData) -> TileGrid:
    width = get_grid_size(tiles_data)

    grid: TileGrid = []
    for _ in range(width):
        grid.append([None]*width)

    solve(tiles, grid)

    return grid

def get_full_image(grid: TileGrid) -> list[str]:
    rows = []
    for y in range(len(grid)):
        row = []
        for x in range(len(grid[0])):
            cell = grid[y][x]
            assert cell
            inner = cell[1].inner
            if x == 0:
                row = inner.copy()
            else:
                for i in range(len(inner)):
                    row[i] += inner[i]
        rows.extend(row)

    return rows

def is_sea_monster(image: list[str], sea_monster: list[str], x: int, y: int) -> bool:
    for oy in range(len(sea_monster)):
        for ox in range(len(sea_monster[0])):
            if sea_monster[oy][ox] == "#" and image[y+oy][x+ox] != "#":
                return False
    return True

def count_symbol(image: list[str], symbol: str) -> int:
    return sum(sum(c == symbol for c in row) for row in image)

def count_sea_monsters(image: list[str], sea_monster: list[str]) -> int:
    monsters = 0

    for y in range(len(image)-len(sea_monster)+1):
        for x in range(len(image[0])-len(sea_monster[0])+1):
            if is_sea_monster(image, sea_monster, x, y):
                monsters += 1

    return monsters

def part2(grid: TileGrid) -> int:
    image = get_full_image(grid)
    sea_monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "
    ]

    max_monsters = 0
    for variant in get_image_variants(sea_monster):
        monsters = count_sea_monsters(image, variant)
        max_monsters = max(max_monsters, monsters)

    return count_symbol(image, "#") - count_symbol(sea_monster, "#") * max_monsters

if __name__ == "__main__":
    tiles = parse_input("input.txt")
    grid = solve_grid(tiles)

    print("part1: ", multiply_corners(grid))
    print("part2: ", part2(grid))
