
def getBuses(filename):
	with open(filename, "r") as f:
		f.readline()
		return {i:int(x) for i, x in enumerate(f.readline().split(",")) if x != "x"}

buses = getBuses("input.txt")
step = list(buses.values())[0]
t = step

for dt, busId in buses.items():
	while (t + dt) % busId != 0:
		t += step
	step *= busId

print(t)