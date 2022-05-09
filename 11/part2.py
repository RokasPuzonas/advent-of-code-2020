
initialState = []
with open("input.txt", "r") as f:
	initialState = f.read().splitlines()

stateWidth = len(initialState[0])
stateHeight = len(initialState)

def areSeatsOccupied(state: list, x, y, dx, dy):
	while True:
		x += dx
		y += dy
		if x < 0 or x >= stateWidth or y < 0 or y >= stateHeight:
			return False
		if state[y][x] == "L":
			return False
		if state[y][x] == "#":
			return True

def getNumOfAdjecentOccupiedSeats(state: list, x, y):
	return areSeatsOccupied(state, x, y, -1, -1) \
			 + areSeatsOccupied(state, x, y,  0, -1) \
			 + areSeatsOccupied(state, x, y, +1, -1) \
			 + areSeatsOccupied(state, x, y, -1,  0) \
			 + areSeatsOccupied(state, x, y, +1,  0) \
			 + areSeatsOccupied(state, x, y, -1, +1) \
			 + areSeatsOccupied(state, x, y,  0, +1) \
			 + areSeatsOccupied(state, x, y, +1, +1)

def computeNextState(state: list):
	nexState = state.copy()
	for y in range(stateHeight):
		newLine = []
		for x in range(stateWidth):
			if state[y][x] == ".":
				newLine.append(".")
			elif state[y][x] == "L":
				occupiedSeats = getNumOfAdjecentOccupiedSeats(state, x, y)
				if occupiedSeats == 0:
					newLine.append("#")
				else:
					newLine.append("L")
			else: # if x == "#"
				occupiedSeats = getNumOfAdjecentOccupiedSeats(state, x, y)
				if occupiedSeats >= 5:
					newLine.append("L")
				else:
					newLine.append("#")
		nexState[y] = "".join(newLine)

	return nexState

def getNumOfOccupiedSeats(state: list):
	count = 0
	for line in state:
		count += line.count("#")
	return count

def printState(state: list):
	print("---------------")
	for line in state:
		print(line)

lastState = initialState
currentState = initialState
while True:
	lastState = currentState
	currentState = computeNextState(currentState)
	if currentState == lastState:
		break

print(getNumOfOccupiedSeats(currentState))
