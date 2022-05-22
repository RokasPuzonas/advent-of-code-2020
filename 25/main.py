
def read_input(filename: str) -> tuple[int, int]:
    with open(filename, "r") as f:
        cards_pub, doors_pub = f.read().splitlines()
        return int(cards_pub), int(doors_pub)

def reverse_loop_size(public_key: int, subject_number: int) -> int:
    key = 1
    loop_size = 0
    while key != public_key:
        loop_size += 1
        key *= subject_number
        key %= 20201227
    return loop_size

def transform_key(subject_number: int, loop_size: int) -> int:
    key = 1
    for _ in range(loop_size):
        key *= subject_number
        key %= 20201227
    return key

def part1(cards_pub: int, doors_pub: int) -> int:
    subject_number = 7
    card_loop_size = reverse_loop_size(cards_pub, subject_number)
    return transform_key(doors_pub, card_loop_size)

if __name__ == "__main__":
    cards_pub, doors_pub = read_input("input.txt")
    print("part1: ", part1(cards_pub, doors_pub))
