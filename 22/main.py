

def read_input(filename: str) -> tuple[list[int], list[int]]:
    with open(filename, "r") as f:
        player1, player2 = f.read().split("\n\n")
        player1_cards = list(int(l) for l in player1.splitlines()[1:])
        player2_cards = list(int(l) for l in player2.splitlines()[1:])
        return (player1_cards, player2_cards)

def play_combat(player1: list[int], player2: list[int]) -> list[int]:
    while len(player1) > 0 and len(player2) > 0:
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)

    return max(player1, player2)

def play_recursive_combat(player1: list[int], player2: list[int]) -> tuple[list[int], bool]:
    seen_games = set()

    while len(player1) > 0 and len(player2) > 0:
        seen_game_value = (",".join(map(str, player1)), ",".join(map(str, player2)))
        if seen_game_value in seen_games:
            return player1, True

        seen_games.add(seen_game_value)

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        player1_won = None
        if len(player1) >= card1 and len(player2) >= card2:
            _, player1_won = play_recursive_combat(player1[:card1], player2[:card2])
        else:
            player1_won = card1 > card2

        if player1_won:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)

    return max(player1, player2), len(player2) == 0

def calculate_score(cards: list[int]) -> int:
    score = 0
    for i in range(len(cards)):
        score += cards[i] * (len(cards)-i)
    return score

def part1(player1: list[int], player2: list[int]) -> int:
    winning_cards = play_combat(player1.copy(), player2.copy())
    return calculate_score(winning_cards)

def part2(player1: list[int], player2: list[int]) -> int:
    winning_cards, _ = play_recursive_combat(player1.copy(), player2.copy())
    return calculate_score(winning_cards)

if __name__ == "__main__":
    player1, player2 = read_input("input.txt")
    print("part1: ", part1(player1, player2))
    print("part2: ", part2(player1, player2))
