
def getInstructions(filename):
	with open(filename, "r") as f:
		return list(line.split(" = ") for line in f.read().split("\n"))

def decToBin(decimal):
	binary = bin(decimal)[2:]
	return "0"*(36 - len(binary)) + binary

def applyMask(address, mask):
	return "".join(mask[i] if mask[i] in ["X", "1"] else address[i] for i in range(36))

def writeToMemory(memory, address: str, value):
	numOfFloatingBits = address.count("X")
	for i in range(2**numOfFloatingBits):
		realAddress = address
		for j in range(numOfFloatingBits):
			realAddress = realAddress.replace("X", str((i & 2**j) >> j), 1)
		memory[int(realAddress, 2)] = value

memory = {}
currentMask = "X" * 36
instructions = getInstructions("input.txt")
for instruction in instructions:
	if instruction[0] == "mask":
		currentMask = instruction[1]
	else:
		address = int(instruction[0][4:-1])
		value = int(instruction[1])
		maskedAddress = applyMask(decToBin(address), currentMask)
		writeToMemory(memory, maskedAddress, value)

memorySum = sum(memory.values())
print(memorySum)