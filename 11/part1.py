
initialState = []
with open("input.txt", "r") as f:
	initialState = f.read().splitlines()

stateWidth = len(initialState[0])
stateHeight = len(initialState)

def isSeatOccupied(state: list, x, y):
	if x >= 0 and x < stateWidth and y >= 0 and y < stateHeight:
		return state[y][x] == "#"
	else:
		return False

def getNumOfAdjecentOccupiedSeats(state: list, x, y):
	return isSeatOccupied(state, x-1, y-1) \
			 + isSeatOccupied(state, x  , y-1) \
			 + isSeatOccupied(state, x+1, y-1) \
			 + isSeatOccupied(state, x-1, y  ) \
			 + isSeatOccupied(state, x+1, y  ) \
			 + isSeatOccupied(state, x-1, y+1) \
			 + isSeatOccupied(state, x  , y+1) \
			 + isSeatOccupied(state, x+1, y+1)

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
				if occupiedSeats >= 4:
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

lastState = initialState
currentState = initialState
while True:
	lastState = currentState
	currentState = computeNextState(currentState)
	if currentState == lastState:
		break

print(getNumOfOccupiedSeats(currentState))
