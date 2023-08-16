
def getRuckSacks():
    with open('adventofcode.com_2022_day_3_input.txt', 'r') as file:
        rucksacks = []
        numRuckSacks = 0
        for i in file.readlines():
            numRuckSacks += 1
            if i[-1] == '\n':
                rucksacks.append((numRuckSacks, i[:-1]))
            else:
                rucksacks.append((numRuckSacks, i))
    return rucksacks


def compareDepartments(sack: list):
    duplicates = []
    for i in range(int(len(sack)/2)):
        for j in range(int(len(sack)/2)):
            if sack[i] == sack[int(len(sack)/2)+j] and sack[i] not in duplicates:
                duplicates.append(sack[i])
    return duplicates


def compare3Groups(sacks: list):
    splits = []
    for i in range(len(sacks)):
        splits.append([])
        for j in sacks[i][0]:
            splits[i].append(j)

    return set(splits[0]).intersection(splits[1], splits[2])


def prioritizeItems(duplicateItems: list):
    prioritizeItemsList = []
    for i in duplicateItems:
        if i.islower():
            prioritizeItemsList.append((i, ord(i)-ord("z")+26))
        elif i.isupper():
            prioritizeItemsList.append((i, ord(i)-ord("Z")+52))
    return prioritizeItemsList

# Part 1


def sumPriorities():
    rucksacks = getRuckSacks()
    sumSacks = 0
    for aSack in rucksacks:
        duplicates = compareDepartments(aSack[1])
        prioritized = prioritizeItems(duplicates)
        for prioritize in prioritized:
            sumSacks += prioritize[1]
    return sumSacks

# Part 2


def sumPrioritiesOfGroups():
    ruckSacks = getRuckSacks()
    sumSacks = 0
    for aSack in range(0, len(ruckSacks), 3):
        duplicates = compare3Groups(
            [[ruckSacks[aSack][1]], [ruckSacks[aSack+1][1]], [ruckSacks[aSack+2][1]]])
        prioritized = prioritizeItems(duplicates)
        for prioritize in prioritized:
            sumSacks += prioritize[1]
    return sumSacks


if __name__ == "__main__":
    print("The sum of the priorities: {}".format(sumPriorities()))
    print("The sum of the priorities per groups: {}".format(
        sumPrioritiesOfGroups()))
