def findMarker(characters):
    start = 0
    end = 4
    finding = True
    while finding:
        start_of_packet = characters[start:end]
        if isDuplicate(start_of_packet):
            start += 1
            end += 1
        else:
            finding = False
    return end
        

def isDuplicate(characters):
    for i in range(len(characters)-1):
        for j in range(i+1, len(characters)):
            if characters[i] == characters[j]:
                return True
    return False

# Part 1
def solve():
    with open('adventofcode.com_2022_day_6_input.txt', 'r') as file:
        print('{} characters need to be processed before the first start-of-packet marker is detected'.format(findMarker(file.read())))

if __name__ == '__main__':
    solve()