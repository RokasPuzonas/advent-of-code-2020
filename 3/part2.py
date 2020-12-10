
trees = []
with open("input.txt", "r") as f:
	trees = [line[:-1] for line in f.readlines()]

encounteredTrees = 0
maxRows = len(trees)
maxCols = len(trees[0])

def getEncuonteredTrees(right, down):
	encounteredTrees = 0
	x = 0
	for y in range(down, maxRows, down):
		x = (x + right) % maxCols
		if (trees[y][x] == "#"):
			encounteredTrees += 1
	return encounteredTrees


print(
	getEncuonteredTrees(1, 1) *
	getEncuonteredTrees(3, 1) *
	getEncuonteredTrees(5, 1) *
	getEncuonteredTrees(7, 1) *
	getEncuonteredTrees(1, 2)
)