
'''
Returning a list of tuples.
[(x, y)...]
x -> elf number
y ->  total calories
'''
def getListOfElfs():
    with open('adventofcode.com_2022_day_1_input.txt', 'r') as file:
        elfs = []
        numElfs = 0
        totalCal = 0
        for i in file.readlines():
            if i == "\n":
                numElfs +=1
                elfs.append((numElfs, totalCal))
                totalCal = 0
            
            if i != "\n":
                totalCal += int(i.strip('\n'))
    return sorted(elfs, key=lambda x: x[1], reverse=True)


'''
Returning a tuple containing the elf number and it's total calories
'''
def maxCalories():
    return getListOfElfs()[0]


'''
Gathering the top 3 most acquired calories
'''
def getTop3():
    elfs = getListOfElfs()
    sum = 0
    for i in range(0, 3):
        sum += elfs[i][1]
    return sum


if __name__ == "__main__":
    elfNum, totalCal = maxCalories()
    print("Elf number {} is the maximum carrier of a total of {} calories.".format(elfNum, totalCal))
    print("The top 3 total total calory is {}".format(getTop3()))