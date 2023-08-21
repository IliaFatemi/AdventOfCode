from day6 import isDuplicate, findMarker

assert isDuplicate('abcd') == False
assert isDuplicate('abca') == True
assert isDuplicate('abdd') == True
assert isDuplicate('accd') == True

assert findMarker('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
assert findMarker('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
assert findMarker('nppdvjthqldpwncqszvftbrmjlhg') == 6
assert findMarker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
assert findMarker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') ==11