import time
from itertools import permutations

# This is really waaayy over-engineered :D
# It's just wanted to try this out, so it would work
# for any N dimensions
# For this reason it is also a bit slower in general
class ConwayCubes:
	def __init__(self, initialState, dimensions=3):
		self.neighbourOffsets = set(permutations((-1, 0, 1) * dimensions, dimensions))
		self.neighbourOffsets.remove((0,) * dimensions)

		self.dimensions = dimensions
		self.state = set()
		for cube in initialState:
			missingDimensions = dimensions-len(cube)
			if missingDimensions < 0: # Some dimensions need to be removed
				self.state.add(cube[:dimensions])
			else:
				self.state.add(cube + (0,) * missingDimensions)

	@staticmethod
	def addTuples(t1, t2):
		return tuple(sum(x) for x in zip(t1, t2))

	def getNeighbourCount(self, cube):
		count = 0
		for offset in self.neighbourOffsets:
			neighbour = ConwayCubes.addTuples(cube, offset)
			if neighbour in self.state:
				count += 1
		return count

	def simulateCycle(self):
		nextState = set()
		toBeComputedCubes = set()

		for activeCube in self.state:
			toBeComputedCubes.add(activeCube)
			for offset in self.neighbourOffsets:
				neighbour = ConwayCubes.addTuples(activeCube, offset)
				toBeComputedCubes.add(neighbour)
		
		for cube in toBeComputedCubes:
			neighbourCount = self.getNeighbourCount(cube)
			if (cube in self.state and 2 <= neighbourCount <= 3) or neighbourCount == 3:
				nextState.add(cube)

		self.state = nextState

	def simulateCycles(self, n=1):
		for i in range(n):
			self.simulateCycle()

def getInitialState(filename):
	initialState = set()

	with open(filename, "r") as f:
		lines = f.read().split("\n")
		for y in range(len(lines)):
			for x in range(len(lines[y])):
				if lines[y][x] == '#':
					initialState.add((x, y))
	
	return initialState

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

def part1(intialState):
	cubes = ConwayCubes(initialState, 3)
	cubes.simulateCycles(6)
	return len(cubes.state)

def part2(intialState):
	cubes = ConwayCubes(initialState, 4)
	cubes.simulateCycles(6)
	return len(cubes.state)

if __name__ == "__main__":
	initialState = getInitialState("input.txt")
	start = time.perf_counter()
	print("Part 1: ", part1(initialState))
	print("Part 2: ", part2(initialState))
	end = time.perf_counter()
	print("Runtime {:.3f}".format(end-start))
