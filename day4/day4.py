def getInput():
    with open('adventofcode.com_2022_day_4_input.txt', 'r') as file:
        data = []
        section = 0
        for i in file.readlines():
            if i[-1] == '\n':
                section += 1
                data.append((section, i[:-1].split(',')))
            else:
                section += 1
                data.append((section, i.split(',')))
    return data


def isInRange(data):
    ranges = data[1]
    x1, x2 = map(int, ranges[0].split('-'))
    y1, y2 = map(int, ranges[1].split('-'))
    return (x1 <= y1 and x2 >= y2) or (x1 >= y1 and x2 <= y2)

def isOverlapping(data):
    ranges = data[1]
    x1, x2 = map(int, ranges[0].split('-'))
    y1, y2 = map(int, ranges[1].split('-'))
    return (y1 >= x1 and y1 <= x2) or (y2 >= x1 and y2 <= x2) or (x1 >= y1 and x1 <= y2) or (x2 >= y1 and x2 <= y2)

# part 1
def numPairs():
    dataSet = getInput()
    pairs = 0
    for data in dataSet:
        if isInRange(data):
            pairs += 1
    return pairs

# part 2
def numOverlap():
    dataSet = getInput()
    overlapped = 0
    for data in dataSet:
        if isOverlapping(data):
            overlapped += 1
    return overlapped


if __name__ == "__main__":
    print("Number of pairs: {}".format(numPairs()))
    print("Number of overlaps: {}".format(numOverlap()))