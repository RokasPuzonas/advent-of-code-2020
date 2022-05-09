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

countMemo = {}
def getTotalBagCount(color):
	if countMemo.get(color) == None:
		countMemo[color] = 0
		for bag in rules[color].items():
			countMemo[color] += (getTotalBagCount(bag[0]) + 1) * bag[1]
	return countMemo[color]

print(getTotalBagCount("shiny gold"))
