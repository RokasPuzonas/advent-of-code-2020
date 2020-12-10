
answers = []
with open("input.txt", "r") as f:
	answers = f.read().split("\n\n")

possibleAnswers = "qwertyuiopasdfghjklzxcvbnm"

totalGroupYesCount = 0
for answer in answers:
	for possibleAnswer in possibleAnswers:
		totalGroupYesCount += answer.find(possibleAnswer) > -1
print(totalGroupYesCount)