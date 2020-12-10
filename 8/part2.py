import re

lines = []
with open("input.txt", "r") as f:
	lines = f.read().split("\n")

def simulate():
	acc = 0
	currentLine = 0
	visitedLines = []
	numOfLines = len(lines)
	while currentLine not in visitedLines and currentLine != numOfLines:
		visitedLines.append(currentLine)
		cmd, num = re.findall(r"(\w{3}) ([-\+]\d+)", lines[currentLine])[0]
		if cmd == "jmp":
			currentLine += int(num)
		elif cmd == "acc":
			acc += int(num)
			currentLine += 1
		else:
			currentLine += 1

	if (currentLine == numOfLines):
		return ("exited", acc)
	else:
		return ("terminated", acc)

# Change between jmp and nop
for i in range(0, len(lines)):
	status, acc = "", 0
	line = lines[i]
	if line.startswith("jmp"):
		lines[i] = "nop" + line[3:]
		status, acc = simulate()
		lines[i] = line
	elif line.startswith("nop"):
		lines[i] = "jmp" + line[3:]
		status, acc = simulate()
		lines[i] = line

	if status == "exited":
		print(acc)
		break