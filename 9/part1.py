from itertools import combinations

numbers = []
with open("input.txt") as f:
	numbers = list(int(num) for num in f.read().splitlines())

for i in range(25, len(numbers)):
	possible = False
	for numberPair in combinations(numbers[i-25:i], 2):
		if sum(numberPair) == numbers[i]:
			possible = True
			break
	if not possible:
		print(numbers[i])
		break
