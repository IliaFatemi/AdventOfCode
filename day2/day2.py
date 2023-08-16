'''
opponent:

A --> Rock
B --> Paper
C --> Scissor

user: 

X --> Rock
Y --> Paper
Z --> Scissor

X --> loose
Y --> draw
Z --> win

Round Verdict:
Win --> 6
Draw --> 3
Loose --> 0
'''


def getPuzzleInput():
    with open('adventofcode.com_2022_day_2_input.txt', 'r') as file:
        game_Rounds = []
        for i in file.readlines():
            round_outputs = i.strip('\n').split(' ')
            game_Rounds.append((round_outputs[0], round_outputs[1]))
    return game_Rounds


def RoundVerdict(opponent, user):
    if (user == 'X' and opponent == 'A') or (user == 'Y' and opponent == 'B') or (user == 'Z' and opponent == 'C'):
        return 3
    elif (user == 'X' and opponent == 'C') or (user == 'Y' and opponent == 'A') or (user == 'Z' and opponent == 'B'):
        return 6
    else:
        return 0


def userScoreRule(user):
    if user == 'X':
        return 1
    elif user == 'Y':
        return 2
    else:
        return 3


def setToLoose(opponent):
    if opponent == 'A':
        return 'Z'
    elif opponent == 'B':
        return 'X'
    elif opponent == 'C':
        return 'Y'


def setToWin(opponent):
    if opponent == 'A':
        return 'Y'
    elif opponent == 'B':
        return 'Z'
    elif opponent == 'C':
        return 'X'


def setToDraw(opponent):
    if opponent == 'A':
        return 'X'
    elif opponent == 'B':
        return 'Y'
    elif opponent == 'C':
        return 'Z'


# Part 1
def getTotalScore():
    game_rounds = getPuzzleInput()
    total_score = 0

    for opponent, user in game_rounds:
        total_score += (userScoreRule(user) + RoundVerdict(opponent, user))
    return total_score

# Part 2


def cheatRounds():
    game_rounds = getPuzzleInput()
    totalScore = 0

    for opponent, user in game_rounds:
        if user == 'X':
            totalScore += (userScoreRule(setToLoose(opponent)) +
                           RoundVerdict(opponent, setToLoose(opponent)))
        elif user == 'Y':
            totalScore += (userScoreRule(setToDraw(opponent)) +
                           RoundVerdict(opponent, setToDraw(opponent)))
        elif user == 'Z':
            totalScore += (userScoreRule(setToWin(opponent)) +
                           RoundVerdict(opponent, setToWin(opponent)))
    return totalScore


if __name__ == "__main__":
    print("part 1: Total score: {}".format(getTotalScore()))
    print("part 2: Total score: {}".format(cheatRounds()))
