def getInputs() -> tuple[list, list]:
    crates = []
    instructions = []
    with open('adventofcode.com_2022_day_5_input.txt', 'r') as file:
        newLine = False
        for i in file.readlines():
                if newLine == False:
                    crates.append(i.strip('\n').strip('').split())
                    if i == '\n':
                        newLine = True
                        crates.pop()
                else:
                    instructions.append(i)
    return crates, instructions

# def solve():
#     crates, instructions = getInputs()

#     for commands in instructions:
#         purifiedCommand = commands.split()
#         purifiedCommand.remove('move')
#         purifiedCommand.remove('from')
#         purifiedCommand.remove('to')
#         moveQuantity, fromPos, toPos= purifiedCommand
        
#         print(moveQuantity, fromPos, toPos)

if __name__ == "__main__":
    print(solve())