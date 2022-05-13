Rule = list[list[int]]|str
RulesDict = dict[int, Rule]

def parse_rule(rule_str: str) -> Rule:
    if "\"" in rule_str:
        return rule_str[1]
    else:
        rule = []
        for sequence in rule_str.split(" | "):
            rule.append(list(int(n) for n in sequence.split(" ")))
        return rule

def parse_rules(rules_str: str) -> RulesDict:
    rules = {}
    for line in rules_str.splitlines():
        id_sep = line.find(":")
        id = int(line[:id_sep])
        rules[id] = parse_rule(line[id_sep+2:])
    return rules

def parse_input(filename: str) -> tuple[RulesDict, list[str]]:
    content = None
    with open(filename, "r") as f:
        content = f.read()

    rules_part, messages_part = content.split("\n\n")
    rules = parse_rules(rules_part)
    messages = messages_part.splitlines()
    return rules, messages

def find_match(message: str, rule_id, all_rules: RulesDict) -> list[int]:
    rule = all_rules[rule_id]
    if isinstance(rule, str):
        if message.startswith(rule):
            return [1]
        else:
            return []

    result = []
    for sequence in rule:
        branch = [0]
        for id in sequence:
            new_branch = []
            for last_pos in branch:
                match = find_match(message[last_pos:], id, all_rules)
                for pos in match:
                    new_branch.append(pos + last_pos)
            branch = new_branch
        result += branch
    return result

def matches_zero_rule(message, rules: RulesDict):
    return len(message) in find_match(message, 0, rules)

def part1(rules: RulesDict, messages):
    count = 0
    for message in messages:
        if matches_zero_rule(message, rules):
            count += 1
    return count

def part2(rules: RulesDict, messages):
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    return part1(rules, messages)

if __name__ == "__main__":
    rules, messages = parse_input("input.txt")

    print("part1: ", part1(rules, messages))
    print("part2: ", part2(rules, messages))
