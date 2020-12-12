

def getInstructions(filename):
	with open(filename, "r") as f:
		return [(line[0], int(line[1:])) for line in f.read().split()]

def directionToOffset(direction):
	if direction == "E":
		return (1, 0)
	elif direction == "N":
		return (0, -1)
	elif direction == "W":
		return (-1, 0)
	elif direction == "S":
		return (0, 1)
	else:
		raise Exception(f"Invalid cardinal direction '{direction}'")

def degreesToOffset(degrees):
	degrees %= 360
	if degrees == 0:
		return (1, 0)
	elif degrees == 90:
		return (0, -1)
	elif degrees == 180:
		return (-1, 0)
	elif degrees == 270:
		return (0, 1)
	else:
		raise Exception(f"Invalid degrees '{degrees}'")

if __name__ == "__main__":
	currentDirection = 0
	currentX, currentY = 0, 0
	for instruction in getInstructions("input.txt"):
		opcode, value = instruction
		if opcode == "L":
			currentDirection += value
		elif opcode == "R":
			currentDirection -= value
		else:
			dirX, dirY = 0, 0
			if opcode == "F":
				dirX, dirY = degreesToOffset(currentDirection)
			elif opcode == "B":
				dirX, dirY = degreesToOffset(currentDirection)
				dirX, dirY = -dirX, -dirY
			else:
				dirX, dirY = directionToOffset(opcode)
			currentX += dirX * value
			currentY += dirY * value
	print(abs(currentX) + abs(currentY))

