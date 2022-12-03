# Column 1 is OPPONENTS MOVE
# A = ROCK
# B = PAPER
# C = SCISSORS

# Column 2 is correct response
# X = ROCK
# Y = PAPER
# Z = SCISSORS

# Single round
#   Score of the shape I selected (1 = Rock, 2 = Paper, 3 = Scissor) 
#   + Score for the outcome of the round (0 = lost, 3 = draw, 6 = Win)
# OUTPUT sum of scores for each round

def getOutcome(playerMove, opponentMove):
    if playerMove == "X":
        if opponentMove == "A":
            return 3
        elif opponentMove == "B":
            return 0
        return 6
    elif playerMove == "Y":
        if opponentMove == "A":
            return 6
        elif opponentMove == "B":
            return 3
        return 0
    else:
        if opponentMove == "A":
            return 0
        elif opponentMove == "B":
            return 6
        return 3

def playerMoveValueMap(move):
    if move == "X":
        return 1
    if move == "Y":
        return 2
    return 3

f = open("input.txt", "r")
rounds = f.readlines()

total_score = 0

for round in rounds:
    moves = round.split()
    opponentMove = moves[0]
    playerMove = moves[1]
    total_score += playerMoveValueMap(playerMove) + getOutcome(playerMove, opponentMove)

print(total_score)