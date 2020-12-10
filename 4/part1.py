import re

documents = []
with open("input.txt", "r") as f:
	documents = f.read()

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

numOfValidDocuments = 0
for document in documents.split("\n\n"):
	fields = re.findall(r"(\w+):[^\s]+", document)
	hasAllRequiredFields = True
	for requiredField in requiredFields:
		if requiredField not in fields:
			hasAllRequiredFields = False
			break
	if hasAllRequiredFields:
		numOfValidDocuments += 1

print(numOfValidDocuments)
