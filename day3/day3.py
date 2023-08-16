
def getRuckSacks():
    with open('adventofcode.com_2022_day_3_input.txt', 'r') as file:
        rucksacks = []
        numRuckSacks = 0
        for i in file.readlines():
            numRuckSacks += 1
            rucksacks.append((numRuckSacks, i))
    return rucksacks

def compareDepartments(sack):
    duplicates = []
    for i in range(int(len(sack)/2)):
        for j in range(int(len(sack)/2)):
            if sack[i] == sack[int(len(sack)/2)+j] and sack[i] not in duplicates:
                duplicates.append(sack[i])
    return duplicates

# def findDuplicates():
#     ruckSacks = getRuckSacks()
#     for aSack in ruckSacks:
#         for i in aSack[1]:
#             pass
            
            
if __name__ == "__main__":
    pass