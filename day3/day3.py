
def getRuckSacks():
    with open('adventofcode.com_2022_day_3_input.txt', 'r') as file:
        rucksacks = []
        numRuckSacks = 0
        for i in file.readlines():
            numRuckSacks += 1
            rucksacks.append((numRuckSacks, i))
    return rucksacks
            
            
if __name__ == "__main__":
    pass