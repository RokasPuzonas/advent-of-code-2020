

def getStartingNumbers(filename):
	with open(filename, "r") as f:
		return [int(n) for n in f.read().split(",")]

numbers = getStartingNumbers("input.txt")
positions = {n: i for i,n in enumerate(numbers)}
diff = {n: 0 for n in numbers}

lastNumber = numbers[-1]
#         30000000
targetI = 30000000

i = len(numbers)-1
while i+1 < targetI:
    number = -1
    if lastNumber in diff:
        number = diff[lastNumber]
    else:
        number = 0
    i += 1
    if number in positions:
        diff[number] = i - positions[number]
    positions[number] = i
    lastNumber = number

print(lastNumber)
