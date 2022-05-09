import re

rawRules = ""
with open("input.txt", "r") as f:
	rawRules = f.read()

rules = {}
for rawRule in rawRules.splitlines():
	bags = re.findall(r"(\d+)? ?(\w+ \w+) bag", rawRule)
	targetColor = bags[0][1]

	rules[targetColor] = {}
	if (bags[1][1] != "no other"):
		for bag in bags[1:]:
			rules[targetColor][bag[1]] = int(bag[0])

shinyGoldMemo = {}
def doesContainShinyGold(color):
	if shinyGoldMemo.get(color) == None:
		for nestedColor in rules[color].keys():
			if nestedColor == "shiny gold" or doesContainShinyGold(nestedColor):
				shinyGoldMemo[color] = True
				break
		if shinyGoldMemo.get(color) == None:
			shinyGoldMemo[color] = False
	return shinyGoldMemo[color]

# Populate memo
for color in rules.keys():
	doesContainShinyGold(color)

print(sum(shinyGoldMemo.values()))
