
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
        # take 3 cups
        taken_cups = take_cups(cups, cups.index(current_cup_label)+1, 3)

        # determine destination cup
        destination_label = current_cup_label - 1
        while destination_label not in cups:
            destination_label -= 1
            if destination_label < min_value:
                destination_label = max_value
        destination = cups.index(destination_label)

        # put back the 3 taken cups
        put_cups(cups, destination + 1, taken_cups)

        # move current cup
        current_cup_label = cups[(cups.index(current_cup_label) + 1) % len(cups)]

def simulate_lookup(next_cup_lookup: list[int], current_cup: int, moves: int):
    max_value = len(next_cup_lookup) - 1
    min_value = 1

    for _ in range(moves):
        # take 3 cups
        taken_cup1 = next_cup_lookup[current_cup]
        taken_cup2 = next_cup_lookup[taken_cup1]
        taken_cup3 = next_cup_lookup[taken_cup2]

        # determine destination cup
        destination = current_cup
        while True:
            destination -= 1
            if destination < min_value:
                destination = max_value
            if destination != taken_cup1 and destination != taken_cup2 and destination != taken_cup3:
                break

        # put back the 3 taken cups
        next_cup_lookup[current_cup] = next_cup_lookup[taken_cup3]
        after_destination = next_cup_lookup[destination]
        next_cup_lookup[taken_cup3] = after_destination
        next_cup_lookup[destination] = taken_cup1

        # move current cup
        current_cup = next_cup_lookup[current_cup]

def part1(cups: list[int]) -> str:
    simulate(cups, 100)

    num1_index = cups.index(1)
    return "".join(map(str, cups[num1_index+1:])) + "".join(map(str, cups[:num1_index]))

def part2(cups: list[int]) -> int:
    # create lookup table for the next value
    next_cup_lookup: list[int] = [0]*(len(cups)+1)
    max_value = max(cups)
    cups.append(max_value+1)
    for i in range(len(cups)-1):
        cup = cups[i]
        next_cup = cups[i+1]
        next_cup_lookup[cup] = next_cup

    for next_cup in range(max_value+2, 1_000_000+1):
        next_cup_lookup.append(next_cup)
    next_cup_lookup.append(cups[0])

    # perform the simulation
    simulate_lookup(next_cup_lookup, cups[0], 10_000_000)

    # calculate the final result
    star1 = next_cup_lookup[1]
    star2 = next_cup_lookup[star1]
    return star1 * star2

if __name__ == "__main__":
    cups = read_input("input.txt")
    print("part1: ", part1(cups.copy()))
    print("part2: ", part2(cups.copy()))
