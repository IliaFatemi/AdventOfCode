from day6 import isDuplicate, findMarker, preProcessNum

assert isDuplicate('abcd') == False
assert isDuplicate('abca') == True
assert isDuplicate('abdd') == True
assert isDuplicate('accd') == True

assert findMarker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4) == 7
assert findMarker('bvwbjplbgvbhsrlpgdmjqwftvncz', 4) == 5
assert findMarker('nppdvjthqldpwncqszvftbrmjlhg', 4) == 6
assert findMarker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4) == 10
assert findMarker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4) ==11

assert findMarker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19
assert findMarker('bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23
assert findMarker('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
assert findMarker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
assert findMarker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26