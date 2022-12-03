# Column 1 is OPPONENTS MOVE
# A = ROCK
# B = PAPER
# C = SCISSORS

# Column 2 is how the round needs to end
# X = lose
# Y = draw
# Z = Win

# Single round
#   Score of the shape I selected (1 = Rock, 2 = Paper, 3 = Scissor) 
#   + Score for the outcome of the round (0 = lost, 3 = draw, 6 = Win)
# OUTPUT sum of scores for each round

winLoseTieGuide = {
    "A": {
        "win": "B",
        "lose": "C"
    },
    "B": {
        "win": "C",
        "lose": "A"
    },
    "C": {
        "win": "A",
        "lose": "B"
    }
}

def getRoundResultValue(result):
    if result == "X":
        return 0
    if result == "Y":
        return 3
    return 6

def getMoveValue(move):
    if move == "A":
        return 1
    elif move == "B":
        return 2
    return 3

def getMove(opponent_move, round_result):
    if round_result == "X":
        # LOSE
        return winLoseTieGuide[opponent_move]["lose"]
    elif round_result == "Z":
        # WIN
        return winLoseTieGuide[opponent_move]["win"]

    # TIE
    return opponent_move



f = open("input.txt", "r")
rounds = f.readlines()
total_score = 0

for round in rounds:
    opponent_move, result = round.split()
    playerMove = getMove(opponent_move, result)

    total_score += getMoveValue(playerMove) + getRoundResultValue(result)

print(total_score)
    
