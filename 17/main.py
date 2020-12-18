import time

neighbourOffsets = set()
for x in range(-1, 2):
	for y in range(-1, 2):
		for z in range(-1, 2):
			neighbourOffsets.add((x, y, z))
neighbourOffsets.remove((0, 0, 0))


def getInitialState(filename):
	initialState = set()

	with open(filename, "r") as f:
		lines = f.read().split("\n")
		for y in range(len(lines)):
			for x in range(len(lines[y])):
				if lines[y][x] == '#':
					initialState.add((x, y, 0))
	
	return initialState

def getNeighbourCount(state, spot):
	count = 0
	for offset in neighbourOffsets:
		neighbour = (
			spot[0] + offset[0],
			spot[1] + offset[1],
			spot[2] + offset[2]
		)
		if neighbour in state:
			count += 1
	return count

def isNextCubeStateActive(state, spot):
	neighbourCount = getNeighbourCount(state, spot)
	
	if spot in state:
		return neighbourCount == 3 or neighbourCount == 2
	elif neighbourCount == 3:
		return True
	else:
		return False

def simulateNextState(state):
	nextState = set()
	computedSpots = set()
	
	for activeSpot in state:
		if activeSpot not in computedSpots:
			computedSpots.add(activeSpot)
			if isNextCubeStateActive(state, activeSpot):
				nextState.add(activeSpot)

		for offset in neighbourOffsets:
			neighbourSpot = (
				activeSpot[0] + offset[0],
				activeSpot[1] + offset[1],
				activeSpot[2] + offset[2]
			)
			if neighbourSpot not in computedSpots:
				computedSpots.add(neighbourSpot)
				if isNextCubeStateActive(state, neighbourSpot):
					nextState.add(neighbourSpot)

	return nextState

def vizualizeState(state):
	xLayers = set(spot[0] for spot in state)
	yLayers = set(spot[1] for spot in state)
	zLayers = set(spot[2] for spot in state)

	xMin, xMax = min(xLayers), max(xLayers)
	yMin, yMax = min(yLayers), max(yLayers)
	for z in sorted(zLayers):
		print(f"z={z}")
		for y in range(yMin, yMax+1):
			print("".join('#' if (x, y, z) in state else '.' for x in range(xMin, xMax+1)))
		print()

def simulateCycles(initialState, count=1):
	state = initialState
	for _ in range(6):
		state = simulateNextState(state)
	return state

def part1(intialState):
	return len(simulateCycles(initialState, 6))

def part2(intialState):
	pass

if __name__ == "__main__":
	initialState = getInitialState("input.txt")
	start = time.perf_counter()
	print("Part 1: ", part1(initialState))
	end = time.perf_counter()
	print("Runtime {:.3f}".format(end-start))
