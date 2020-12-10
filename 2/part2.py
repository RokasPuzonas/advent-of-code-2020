import re

passwords = ""
with open("input.txt", "r") as f:
	passwords = "".join(f.readlines())

correctPasswords = 0
for pos1, pos2, targetLetter, password in re.findall(r"(\d+)\-(\d+) (\w): (\w+)", passwords):
	letter1 = password[int(pos1) - 1]
	letter2 = password[int(pos2) - 1]
	if (letter1 == targetLetter and letter2 != targetLetter) or (letter1 != targetLetter and letter2 == targetLetter):
		correctPasswords += 1

print(correctPasswords)