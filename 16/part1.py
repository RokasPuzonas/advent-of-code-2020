import re

def getInput(filename):
    with open(filename, "r") as f:
        fields, myTicket, nearbyTickets = f.read().split("\n\n")
        myTicket = myTicket.replace("your ticket:\n", "")
        nearbyTickets = nearbyTickets.replace("nearby tickets:\n", "")

        return (
            {m[1]: m[2] for m in re.finditer(r"(.+): ([^\n]+)", fields)},
            [int(n) for n in myTicket.split(",")],
            [[int(n) for n in ticket.split(",") ] for ticket in nearbyTickets.splitlines()]
        )

class FieldRule:
    def __init__(self, raw: str):
        self.raw = raw
        match = re.match(r"(\d+)\-(\d+) or (\d+)\-(\d+)", raw)
        assert match
        self.range1 = [int(match[1]), int(match[2])]
        self.range2 = [int(match[3]), int(match[4])]

    def __call__(self, num: int):
        return (self.range1[0] <= num <= self.range1[1]) or \
                     (self.range2[0] <= num <= self.range2[1])

    def __repr__(self):
        return f'FieldRule("{self.raw}")'

fields, myTicket, nearbyTickets = getInput("input.txt")

for fieldName, fieldRule in fields.items():
	fields[fieldName] = FieldRule(fieldRule)

invalidNumbers = []
for ticket in nearbyTickets:
    for num in ticket:
        if all(not rule(num) for rule in fields.values()): # type: ignore
            invalidNumbers.append(num)

print(sum(invalidNumbers))
