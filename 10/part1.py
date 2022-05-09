
adapters = []
with open("input.txt") as f:
	adapters = list(int(num) for num in f.read().splitlines())

adapters.append(0)
adapters.sort()
adapters.append(adapters[-1]+3)
numOf3Diff = 0
numOf1Diff = 0
print(adapters)
for i in range(0, len(adapters)-1):
	diff = adapters[i+1] - adapters[i]
	if diff == 1:
		numOf1Diff += 1
	elif diff == 3:
		numOf3Diff += 1
print(numOf1Diff * numOf3Diff)
