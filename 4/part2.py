import re

documents = []
with open("input.txt", "r") as f:
	documents = f.read()

requiredFields = {
	"byr": re.compile(r"^(19[2-9][0-9]|200[0-2])$"),
	"iyr": re.compile(r"^(20[1-2][0-9])$"),
	"eyr": re.compile(r"^(202[0-9]|2030)$"),
	"hgt": re.compile(r"^(1([5-8][0-9]|9[0-3])cm)|((59|6[0-9]|7[0-6])in)$"),
	"hcl": re.compile(r"^#[0-9a-f]{6}$"),
	"ecl": re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$"),
	"pid": re.compile(r"^[0-9]{9}$")
}

numOfValidDocuments = 0
for document in documents.split("\n\n"):
	fields = re.findall(r"(\w+):([^\s]+)", document)
	fieldsTable = {}
	for field in fields:
		fieldsTable[field[0]] = field[1]
	hasAllRequiredFields = True
	for fieldName, fieldRegex in requiredFields.items():
		value = fieldsTable.get(fieldName)
		if value == None or not fieldRegex.match(value):
			hasAllRequiredFields = False
			break

	if hasAllRequiredFields:
		numOfValidDocuments += 1

print(numOfValidDocuments)