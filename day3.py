import re
from functools import reduce

with open("input.txt") as f:
    c = f.read()

# part 1
print(sum([int(m[1])*int(m[2]) for m in re.findall(r"(mul\(([0-9]+),([0-9]+)\))", c)]))

# part 2
def f(b, m):
    if m[0] == "do()":
        return (b[0], True)
    elif m[0] == "don't()":
        return (b[0], False)
    elif b[1]:
        return (b[0] + int(m[1]) * int(m[2]), True)
    else:
        return b

print(reduce(lambda acc, m: f(acc, m), re.findall(r"(mul\(([0-9]+),([0-9]+)\)|don't\(\)|do\(\))", c), (0, True))[0])
