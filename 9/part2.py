from itertools import combinations

preamble_size = 25

numbers = []
with open("input.txt") as f:
	numbers = list(int(num) for num in f.read().splitlines())

def getInvalidNumber():
	for i in range(preamble_size, len(numbers)):
		possible = False
		for numberPair in combinations(numbers[i-preamble_size:i], 2):
			if sum(numberPair) == numbers[i]:
				possible = True
				break
		if not possible:
			return numbers[i]

invalidNumber = getInvalidNumber()
found = False
for setSize in range(2, len(numbers)):
    for setStart in range(0, len(numbers)-setSize, 1):
        contiguos_set = numbers[setStart:setStart+setSize]
        if sum(contiguos_set) == invalidNumber:
            print(min(contiguos_set) + max(contiguos_set))
            found = True
            break
    if found: break
