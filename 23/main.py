
def read_input(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return list(int(c) for c in f.readline()[:-1])

def take_cups(cups: list[int], start: int, length: int) -> list[int]:
    taken_cups = []
    index = start % len(cups)
    for _ in range(length):
        taken_cups.append(cups.pop(index))
        index = index % len(cups)
    return taken_cups

def put_cups(cups: list[int], start: int, target: list[int]):
    index = start
    for value in target:
        cups.insert(index, value)
        index = index + 1

def simulate(cups: list[int], moves: int):
    max_value = max(cups)
    min_value = min(cups)

    current_cup_label = cups[0]
    for _ in range(moves):
        taken_cups = take_cups(cups, cups.index(current_cup_label)+1, 3)

        destination_label = current_cup_label - 1
        while destination_label not in cups:
            destination_label -= 1
            if destination_label < min_value:
                destination_label = max_value
        destination = cups.index(destination_label)

        put_cups(cups, destination + 1, taken_cups)

        current_cup_label = cups[(cups.index(current_cup_label) + 1) % len(cups)]

def part1(cups: list[int]) -> str:
    simulate(cups, 100)

    num1_index = cups.index(1)
    return "".join(map(str, cups[num1_index+1:])) + "".join(map(str, cups[:num1_index]))

def part2(cups: list[int]) -> int:
    for value in range(max(cups), 1_000_000 + 1):
        cups.append(value)

    simulate(cups, 1_00)
    # simulate(cups, 10_000_000)

    num1_index = cups.index(1)
    star1 = cups[(num1_index + 1) % len(cups)]
    star2 = cups[(num1_index + 2) % len(cups)]
    return star1 * star2

if __name__ == "__main__":
    cups = read_input("test.txt")
    print("part1: ", part1(cups.copy()))
    print("part2: ", part2(cups.copy()))
