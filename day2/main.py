
def getPuzzleInput():
    with open('adventofcode.com_2022_day_2_input.txt', 'r') as file:
        game_Rounds = []
        for i in file.readlines():
            round_outputs = i.strip('\n').split(' ')
            game_Rounds.append((round_outputs[0], round_outputs[1]))
    return game_Rounds
    

if __name__ == "__main__":
    getPuzzleInput()