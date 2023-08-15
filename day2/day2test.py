from day2 import RoundVerdict, userScoreRule, setToLoose, setToWin

assert RoundVerdict('A', 'Y') == 6
assert RoundVerdict('B', 'X') == 0
assert RoundVerdict('C', 'Z') == 3

assert userScoreRule('X') == 1
assert userScoreRule('Y') == 2
assert userScoreRule('Z') == 3

assert setToLoose('A') == 'Z'
assert setToLoose('B') == 'X'
assert setToLoose('C') == 'Y'

assert setToWin('A') == 'Y'
assert setToWin('B') == 'Z'
assert setToWin('C') == 'X'