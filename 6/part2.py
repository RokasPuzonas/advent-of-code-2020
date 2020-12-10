
answerGroups = []
with open("input.txt", "r") as f:
	answerGroups = [answerGroup.split("\n") for answerGroup in f.read().split("\n\n")]

possibleAnswers = "qwertyuiopasdfghjklzxcvbnm"

totalGroupYesCount = 0
for answerGroup in answerGroups:
	for possibleAnswer in possibleAnswers:
		totalGroupYesCount += all(answer.find(possibleAnswer) > -1 for answer in answerGroup)
print(totalGroupYesCount)