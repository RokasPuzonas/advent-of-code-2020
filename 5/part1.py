
boardingPasses = []
with open("input.txt", "r") as f:
	boardingPasses = f.read().split("\n")

def decodePass(encoded):
    if len(encoded) == 0: return 0
    row = 0
    row += 64*(encoded[0] == "B")
    row += 32*(encoded[1] == "B")
    row += 16*(encoded[2] == "B")
    row += 8 *(encoded[3] == "B")
    row += 4 *(encoded[4] == "B")
    row += 2 *(encoded[5] == "B")
    row += 1 *(encoded[6] == "B")
    column = 0
    column += 4*(encoded[7] == "R")
    column += 2*(encoded[8] == "R")
    column += 1*(encoded[9] == "R")
    return row * 8 + column

maxBoardingPass = max(decodePass(boardingPass) for boardingPass in boardingPasses)
print(maxBoardingPass)
