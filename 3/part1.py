
trees = []
with open("input.txt", "r") as f:
	trees = [line[:-1] for line in f.readlines()]

encounteredTrees = 0
maxRows = len(trees)
maxCols = len(trees[0])

x = 0
for y in range(1, maxRows):
	x = (x + 3) % maxCols
	if (trees[y][x] == "#"):
		encounteredTrees += 1

print(encounteredTrees)