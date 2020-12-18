import re

def getInput(filename):
	with open(filename, "r") as f:
		fields, myTicket, nearbyTickets = f.read().split("\n\n")
		myTicket = myTicket.replace("your ticket:\n", "")
		nearbyTickets = nearbyTickets.replace("nearby tickets:\n", "")

		return (
			{m[1]: m[2] for m in re.finditer(r"(.+): ([^\n]+)", fields)},
			[int(n) for n in myTicket.split(",")],
			[[int(n) for n in ticket.split(",") ] for ticket in nearbyTickets.split("\n")]
		)

class FieldRule:
	def __init__(self, raw: str):
		self.raw = raw
		match = re.match(r"(\d+)\-(\d+) or (\d+)\-(\d+)", raw)
		self.range1 = [int(match[1]), int(match[2])]
		self.range2 = [int(match[3]), int(match[4])]

	def __call__(self, num: int):
		return (self.range1[0] <= num <= self.range1[1]) or \
					 (self.range2[0] <= num <= self.range2[1])

	def __repr__(self):
		return f'FieldRule("{self.raw}")'

def isFieldValid(tickets, fieldRule, pos):
	for ticket in tickets:
		if not fieldRule(ticket[pos]):
			return False
	return True

# A backtracking algorithm to find the field order
def solveFieldOrder(tickets, fields: dict):
	fieldOrder = {}

	numOfFields = len(fields)
	unassignedFields = fields.copy()
	while len(fieldOrder) < numOfFields:
		possibleFields = {}

		for fieldName, fieldRule in unassignedFields.items():
			for i in range(numOfFields):
				if i not in fieldOrder.values() and isFieldValid(tickets, fieldRule, i):
					possibleFields[fieldName] = possibleFields.get(fieldName, [])
					possibleFields[fieldName].append(i)

		for fieldName, orders in possibleFields.items():
			if len(orders) == 1:
				fieldOrder[fieldName] = orders[0]
				del unassignedFields[fieldName];

	return fieldOrder

fields, myTicket, nearbyTickets = getInput("input.txt")

# Preproccess the ticket so that checking is faster
for fieldName, fieldRule in fields.items():
	fields[fieldName] = FieldRule(fieldRule)

# Filter out the invalid tickets
validNearbyTickets = []
for ticket in nearbyTickets:
	isTicketValid = True
	for num in ticket:
		if all(not rule(num) for rule in fields.values()):
			isTicketValid = False
			break
	if isTicketValid:
		validNearbyTickets.append(ticket)

# Find combination of fields that is valid
fieldOrder = solveFieldOrder(validNearbyTickets, fields)

solution = 1
for fieldName, order in fieldOrder.items():
	if fieldName.startswith("departure"):
		solution *= myTicket[order]

print(solution)