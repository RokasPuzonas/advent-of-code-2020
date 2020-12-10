from itertools import combinations

expenseReports = []
with open("input.txt", "r") as f:
	expenseReports = [int(line[:-1]) for line in f.readlines()]

for expensePair in combinations(expenseReports, 2):
	if sum(expensePair) == 2020:
		print(expensePair[0] * expensePair[1])
		break
