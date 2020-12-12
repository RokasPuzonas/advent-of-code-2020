import math

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

def rotatePoint(x, y, angle):
	angleRadians = math.radians(angle)
	return round(x * math.cos(angleRadians) - y * math.sin(angleRadians)), \
				 round(x * math.sin(angleRadians) + y * math.cos(angleRadians))

if __name__ == "__main__":
	currentX, currentY = 0, 0
	waypointX, waypointY = 10, -1
	for instruction in getInstructions("input.txt"):
		opcode, value = instruction
		if opcode == "F":
			currentX += waypointX * value
			currentY += waypointY * value
		elif opcode == "L":
			waypointX, waypointY = rotatePoint(waypointX, waypointY, -value)
		elif opcode == "R":
			waypointX, waypointY = rotatePoint(waypointX, waypointY, value)
		else:
			offX, offY = directionToOffset(opcode)
			waypointX += offX * value
			waypointY += offY * value
	print(abs(currentX) + abs(currentY))