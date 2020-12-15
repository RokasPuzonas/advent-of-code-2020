

def getStartingNumbers(filename):
	with open(filename, "r") as f:
		return [int(n) for n in f.read().split(",")]

numbers = getStartingNumbers("input.txt")
occurences = {n: [i] for i,n in enumerate(numbers)}
lastNumber = numbers[-1]
#         30000000
targetI = 30000000
i = len(numbers)-1
while i+1 < targetI:
	if len(occurences[lastNumber]) > 1:
		number = occurences[lastNumber][-1] - occurences[lastNumber][-2]
	else:
		number = 0
	i += 1
	occurences[number] = occurences.get(number, [])
	occurences[number].append(i)
	occurences[number] = occurences[number][-2:]
	lastNumber = number

print(lastNumber)