
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
             
            
    return elfs

def maxCalories(ListofElfs):
    pass
    


if __name__ == "__main__":
    # print("Elf number {} is carrying a total of {} calories.".format(maxCalories()))
    print(getListOfElfs())