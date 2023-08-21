def findMarker(characters):
    start = 0
    end = 3
    finding = True
    while finding:
        pass

def isDuplicate(characters):
    for i in range(len(characters)-1):
        for j in range(i+1, len(characters)):
            if characters[i] == characters[j]:
                return True
    return False
