import math

def getNotes(filename):
	with open(filename, "r") as f:
		return {
			"departTime": int(f.readline()),
			"IDs": [int(i) for i in f.readline().split(",") if i != "x"]
		}

notes = getNotes("input.txt")
departTime = notes["departTime"]
earliestID = 0
earliestTime = math.ceil(departTime/notes["IDs"][0])*notes["IDs"][0]
for ID in notes["IDs"]:
	time = math.ceil(departTime/ID)*ID
	if earliestTime > time:
		earliestTime = time
		earliestID = ID

print(earliestID*(earliestTime-departTime))