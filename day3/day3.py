
def getRuckSacks():
    with open('adventofcode.com_2022_day_3_input.txt', 'r') as file:
        rucksacks = []
        numRuckSacks = 0
        for i in file.readlines():
            numRuckSacks += 1
            rucksacks.append((numRuckSacks, i))
    return rucksacks

def compareDepartments(sack: list):
    duplicates = []
    for i in range(int(len(sack)/2)):
        for j in range(int(len(sack)/2)):
            if sack[i] == sack[int(len(sack)/2)+j] and sack[i] not in duplicates:
                duplicates.append(sack[i])
    return duplicates

def compareGroups(sacks: list):
    pass

def prioritizeItems(duplicateItems: list):
    prioritizeItemsList = []
    for i in duplicateItems:
        if i.islower():
            prioritizeItemsList.append((i, ord(i)-ord("z")+26))
        elif i.isupper():
            prioritizeItemsList.append((i, ord(i)-ord("Z")+52))
    return prioritizeItemsList

#Part 1
def sumPriorities():
    rucksacks = getRuckSacks()
    sumSacks = 0
    for aSack in rucksacks:
        duplicates = compareDepartments(aSack[1])
        prioritized = prioritizeItems(duplicates)
        for prioritize in prioritized:
            sumSacks += prioritize[1]
    return sumSacks

#Part 2

            
if __name__ == "__main__":
    print("The sum of the priorities: {}".format(sumPriorities()))