def getInputs() -> tuple[list, list]:
    crates = []
    instructions = []
    with open('adventofcode.com_2022_day_5_input.txt', 'r') as file:
        newLine = False
        for i in file.readlines():
                if newLine == False:
                    crates.append(i.strip('\n').split(' '))
                    if i == '\n':
                        newLine = True
                        crates.pop()
                else:
                    instructions.append(i)
        print(rotateMatrix(crates))
        print()
    return crates, instructions

def cratify(crates):
    newCrate = []
    row = 0
    flag = False
    for i in range(len(crates)):
        newCrate.append([])
    
    for crate in crates:
        for item in crate:
            if item == '' and flag == False:
                newCrate[row].append('')
                flag = True
            elif item != '':
                newCrate[row].append(item)
                flag = False
        row += 1
    newCrate.pop()
    return newCrate


def rotateMatrix(crates):
    newCrate = []
    num_containers = len(crates)-1
    col = 0
    numSpaces = 0
    print(crates)
    print()
    print(cratify(crates))
    
    
    # for i in range(num_containers):
    #     newCrate.append([])
    # for crate in crates:
    #     for item in crate:
    #         if item == '':
    #             numSpaces += 1
    #         if numSpaces == 3:
    #             col += 1
    #             numSpaces = 0
    #         if item != '':
    #             try:
    #                 newCrate[col].append(item)
    #             except IndexError:
    #                 newCrate[col-2].append(item)
    #             finally:
    #                 col += 1
    #                 numSpaces = 0
    #     col = 0
    #     numSpaces = 0
    # for i in newCrate:
    #     i.pop()
    return newCrate
                
    

if __name__ == "__main__":
    getInputs()