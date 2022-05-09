import re

def getExpressions(filename):
	with open(filename, "r") as f:
		return f.read().splitlines()

def findMatchingPosition(line: str, pos: int) -> int:
    depth = 1
    end_pos = pos
    while depth > 0:
        end_pos += 1
        if line[end_pos] == "(":
            depth += 1
        elif line[end_pos] == ")":
            depth -= 1

    return end_pos

def findMatchingParenthesis(line: str) -> list[tuple[int, int]]:
    parens = []
    for match in re.finditer(r"\(", line):
        paren_start = match.start()
        parent_end = findMatchingPosition(line, paren_start)
        parens.append((paren_start, parent_end))
    return parens

def determineTopParenthesis(parens: list[tuple[int, int]]) -> list[tuple[int, int]]:
    top_parens = []
    for i in range(len(parens)):
        is_top_paren = True
        for j in range(len(parens)):
            if i != j and parens[i][0] > parens[j][0] and parens[i][1] < parens[j][1]:
                is_top_paren = False
                break

        if is_top_paren:
            top_parens.append(parens[i])
    return top_parens

def evaluateExpression(expression: str):
    parens = findMatchingParenthesis(expression)
    top_parens = determineTopParenthesis(parens)
    top_parens.sort(key=lambda p: p[0])

    offset = 0
    for paren in top_parens:
        paren_start = paren[0] - offset
        paren_end = paren[1] - offset
        sub_value = evaluateExpression(expression[paren_start+1:paren_end])
        expression = expression[:paren_start] + str(sub_value) + expression[paren_end+1:]
        offset += (paren[1] - paren[0] - len(str(sub_value)) + 1)

    parts = re.findall(r"(\d+|[\*\+])", expression)
    result = int(parts[0])
    for i in range(1, len(parts), 2):
        if parts[i] == "*":
            result *= int(parts[i+1])
        elif parts[i] == "+":
            result += int(parts[i+1])

    return result

def evaluateAdvancedExpression(expression: str) -> int:
    parens = findMatchingParenthesis(expression)
    top_parens = determineTopParenthesis(parens)
    top_parens.sort(key=lambda p: p[0])

    offset = 0
    for paren in top_parens:
        paren_start = paren[0] - offset
        paren_end = paren[1] - offset
        sub_value = evaluateAdvancedExpression(expression[paren_start+1:paren_end])
        expression = expression[:paren_start] + str(sub_value) + expression[paren_end+1:]
        offset += (paren[1] - paren[0] - len(str(sub_value)) + 1)

    parts = re.findall(r"(\d+|[\*\+])", expression)
    i = 1
    while i < len(parts):
        if parts[i] == "+":
            a = parts[i-1]
            b = parts[i+1]
            parts = parts[:i-1] + [int(a) + int(b)] + parts[i+2:]
            i = -1
        i += 2

    result = int(parts[0])
    for i in range(2, len(parts), 2):
        result *= int(parts[i])

    return result

def part1(filename: str) -> int:
    total = 0
    for expression in getExpressions(filename):
        total += evaluateExpression(expression)
    return total

def part2(filename: str) -> int:
    total = 0
    for expression in getExpressions(filename):
        total += evaluateAdvancedExpression(expression)
    return total

if __name__ == "__main__":
    print("Part 1: ", part1("input.txt"))
    print("Part 2: ", part2("input.txt"))
