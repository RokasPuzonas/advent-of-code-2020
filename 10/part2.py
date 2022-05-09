
adapters = []
with open("input.txt") as f:
	adapters = list(int(num) for num in f.read().splitlines())

adapters.append(0)
adapters.sort()
adapters.append(adapters[-1]+3)

memo = {}
memo[adapters[-1]] = 1
def getNumOfCombinations(adapterList):
    if memo.get(adapterList[0]):
         return memo[adapterList[0]]
    combinations = 1
    for i in range(1, len(adapterList)):
        diff = adapterList[i] - adapterList[0]
        if 0 < diff <= 3:
             combinations += getNumOfCombinations(adapterList[i:])
        else:
            break
    combinations = combinations - 1
    memo[adapterList[0]] = combinations
    return combinations

print(getNumOfCombinations(adapters))
