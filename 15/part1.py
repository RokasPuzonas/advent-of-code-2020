


def getStartingNumbers(filename):
	with open(filename, "r") as f:
		return [int(n) for n in f.read().split(",")]

numbers = getStartingNumbers("input.txt")
occurences = {n: [i] for i,n in enumerate(numbers)}

while len(numbers) < 2020:
	lastNumber = numbers[-1]
	if len(occurences[lastNumber]) > 1:
		number = occurences[lastNumber][-1] - occurences[lastNumber][-2]
	else:
		number = 0
	occurences[number] = occurences.get(number, [])
	occurences[number].append(len(numbers))
	numbers.append(number)

print(numbers[2019])