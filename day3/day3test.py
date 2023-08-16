from day3 import compareDepartments, prioritizeItems

assert compareDepartments("vJrwpWtwJgWrhcsFMMfFFhFp") == ["p"]
assert compareDepartments("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == ["L"]
assert compareDepartments("PmmdzqPrVvPwwTWBwg") == ["P"]
assert compareDepartments("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn") == ["v"]
assert compareDepartments("ttgJtRGJQctTZtZT") == ["t"]
assert compareDepartments("CrZsJsPPZsGzwwsLwLmpwMDw") == ["s"]
assert compareDepartments("gjqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSLG") == ["G", "L"]


assert prioritizeItems(["p"]) == [("p", 16)]
assert prioritizeItems(["L"]) == [("L", 38)]
assert prioritizeItems(["p"]) == [("p", 16)]
assert prioritizeItems(["v"]) == [("v", 22)]
assert prioritizeItems(["t"]) == [("t", 20)]
assert prioritizeItems(["s"]) == [("s", 19)]
assert prioritizeItems(["G", "L"]) == [("G", 33), ("L", 38)]
assert prioritizeItems(["Z"]) == [("Z", 52)]
assert prioritizeItems(["z"]) == [("z", 26)]