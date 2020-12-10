from itertools import combinations

numbers = []
with open("input.txt") as f:
	numbers = list(int(num) for num in f.read().split("\n"))

def getInvalidNumber():
	for i in range(25, len(numbers)):
		possible = False
		for numberPair in combinations(numbers[i-25:i], 2):
			if sum(numberPair) == numbers[i]:
				possible = True
				break
		if not possible:
			return numbers[i]

invalidNumber = getInvalidNumber()
found = False
for setSize in range(2, len(numbers)):
	for setStart in range(0, len(numbers)-setSize, 1):
		if sum(numbers[setStart:setStart+setSize]) == invalidNumber:
			print(numbers[setStart] + numbers[setStart+setSize-1])
			found = True
			break
	if found: break
