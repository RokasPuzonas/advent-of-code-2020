import re

passwords = ""
with open("input.txt", "r") as f:
	passwords = "".join(f.readlines())

correctPasswords = 0
for letterMin, letterMax, letter, password in re.findall(r"(\d+)\-(\d+) (\w): (\w+)", passwords):
	letterCount = password.count(letter)
	if int(letterMin) <= letterCount <= int(letterMax):
		correctPasswords += 1
	
print(correctPasswords)