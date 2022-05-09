
answerGroups = []
with open("input.txt", "r") as f:
	answerGroups = [answerGroup.split("\n") for answerGroup in f.read().split("\n\n")]

possibleAnswers = "qwertyuiopasdfghjklzxcvbnm"

totalGroupYesCount = 0
for answerGroup in answerGroups:
    if answerGroup[-1] == "":
        answerGroup.pop()

    answersCounter = {}
    for answers in answerGroup:
        for letter in answers:
            if letter not in answersCounter:
                answersCounter[letter] = 0
            answersCounter[letter] += 1

    for count in answersCounter.values():
        if count == len(answerGroup):
            totalGroupYesCount += 1
print(totalGroupYesCount)
