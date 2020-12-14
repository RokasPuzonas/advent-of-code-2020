

def getInstructions(filename):
	with open(filename, "r") as f:
		return list(line.split(" = ") for line in f.read().split("\n"))

def applyMask(value, mask):
	return (value | int(mask.replace("X", "0"), 2)) & int(mask.replace("X", "1"), 2)

memory = {}
currentMask = "X" * 36
instructions = getInstructions("input.txt")
for instruction in instructions:
	if instruction[0] == "mask":
		currentMask = instruction[1]
	else:
		address = int(instruction[0][4:-1])
		value = int(instruction[1])
		memory[address] = applyMask(value, currentMask)

memorySum = sum(memory.values())
print(memorySum)