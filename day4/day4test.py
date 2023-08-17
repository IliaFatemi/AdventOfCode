from day4 import isInRange

assert isInRange((1, ['2-4', '6-8'])) == False
assert isInRange((2, ['2-3', '4-5'])) == False
assert isInRange((3, ['5-7', '7-9'])) == False
assert isInRange((4, ['2-8', '3-7'])) == True
assert isInRange((5, ['6-6', '4-6'])) == True
assert isInRange((6, ['2-6', '4-8'])) == False