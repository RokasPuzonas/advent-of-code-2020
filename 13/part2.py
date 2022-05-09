
def parseBuses(line):
    return {i:int(x) for i, x in enumerate(line.split(",")) if x != "x"}

def getBuses(filename):
    with open(filename, "r") as f:
        f.readline()
        return parseBuses(f.readline())

buses = getBuses("input.txt")
step = 1
t = 0

for dt, busId in buses.items():
    while (t + dt) % busId != 0:
        t += step
    step *= busId

print(t)
