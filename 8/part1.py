import re

lines = []
with open("input.txt", "r") as f:
	lines = f.read().split("\n")

acc = 0
visitedLines = []
currentLine = 0
while currentLine not in visitedLines:
	visitedLines.append(currentLine)
	cmd, num = re.findall(r"(\w{3}) ([-\+]\d+)", lines[currentLine])[0]
	if cmd == "jmp":
		currentLine += int(num)
	elif cmd == "acc":
		acc += int(num)
		currentLine += 1
	else:
		currentLine += 1

print(acc)