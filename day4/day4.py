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
    x1, x2 = ranges[0].split('-')
    y1, y2 = ranges[1].split('-') 
    return (int(y1) >= int(x1) and int(y2) <= int(x2)) or (int(x1) >= int(y1) and int(y2) <= int(x2))

def numPairs():
    dataSet = getInput()
    pairs = 0
    for data in dataSet:
        if isInRange(data):
            pairs += 1
    return pairs


if __name__ == "__main__":
    print("Number of pairs: {}".format(numPairs()))