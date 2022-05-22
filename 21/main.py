from dataclasses import dataclass

@dataclass
class Food:
    ingredients: list[str]
    allergens: list[str]

def parse_food(line: str) -> Food:
    delim = line.find(" (contains ")
    return Food(
        ingredients=line[:delim].split(" "),
        allergens=line[delim+11:-2].split(", ")
    )

def read_input(filename: str) -> list[Food]:
    with open(filename, "r") as f:
        return list(parse_food(line) for line in f.readlines())

def count_ingredient_occurences(foods: list[Food]) -> dict[str, int]:
    ingredient_counts = {}
    for food in foods:
        for ingredient in food.ingredients:
            ingredient_counts[ingredient] = ingredient_counts.get(ingredient, 0) + 1
    return ingredient_counts

def get_allergen_map(foods: list[Food]) -> dict[str, set[str]]:
    allergen_map = {}
    for food in foods:
        for allergen in food.allergens:
            if allergen in allergen_map:
                allergen_map[allergen] = allergen_map[allergen]&set(food.ingredients)
            else:
                allergen_map[allergen] = set(food.ingredients)
    return allergen_map

def part1(foods: list[Food]) -> int:
    allergen_map = get_allergen_map(foods)

    allergen_ingredients = set()
    for ingredients in allergen_map.values():
        allergen_ingredients.update(ingredients)

    count = 0
    ingredient_counts = count_ingredient_occurences(foods)
    for ingredient in ingredient_counts.keys():
        if ingredient not in allergen_ingredients:
            count += ingredient_counts[ingredient]

    return count

def find_with_one_ingredient(allergen_map: dict[str, set[str]]) -> tuple[str, str]|None:
    for allergen, ingredients in allergen_map.items():
        if len(ingredients) == 1:
            # `min` is used just, because you can't use indexing on sets
            return (allergen, min(ingredients))

def part2(foods: list[Food]) -> str:
    allergen_map = get_allergen_map(foods)
    allergens = []
    while True:
        pair = find_with_one_ingredient(allergen_map)
        if pair == None:
            break
        allergens.append(pair)
        allergen, ingredient = pair
        del allergen_map[allergen]
        for ingredients in allergen_map.values():
            if ingredient in ingredients:
                ingredients.remove(ingredient)

    allergens.sort(key=lambda p: p[0])

    return ",".join(a[1] for a in allergens)

if __name__ == "__main__":
    foods = read_input("input.txt")
    print("part1: ", part1(foods))
    print("part2: ", part2(foods))
