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




if __name__ == "__main__":
    print(getInput())