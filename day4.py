import numpy as np
import re

with open("input.txt") as f:
    c = f.readlines()
# part 1
s = sum([len(re.findall(r"XMAS", l)) for l in c]) # left to right

b = np.array(list(map(list, c)))
s += sum([len(re.findall(r"XMAS", l)) for l in list(map(lambda x: "".join(list(x)), b[:, ::-1]))]) # right to left
s += sum([len(re.findall(r"XMAS", l)) for l in list(map(lambda x: "".join(list(x)), b.T))]) # top to bottom
s += sum([len(re.findall(r"XMAS", l)) for l in list(map(lambda x: "".join(list(x)), b.T[:, ::-1]))]) # bottom to top

d1 = [np.diag(b, diag) for diag in range(-(b.shape[0] - 1), b.shape[1])]
s += sum([len(re.findall(r"XMAS", l)) for l in list(map(lambda x: "".join(list(x)), d1))]) # diag left to right
s += sum([len(re.findall(r"XMAS", l)) for l in list(map(lambda x: "".join(list(x)[::-1]), d1))]) # reverse diag left to right

d2 = [np.diag(b[:, ::-1], diag) for diag in range(-(b[:, ::-1].shape[0] - 1), b[:, ::-1].shape[1])]
s += sum([len(re.findall(r"XMAS", l)) for l in list(map(lambda x: "".join(list(x)), d2))]) # diag right to left
s += sum([len(re.findall(r"XMAS", l)) for l in list(map(lambda x: "".join(list(x)[::-1]), d2))]) # reverse diag right to left
print(s)

# part 2
s = 0
for i in range(1, len(c) - 1):
    for j in range(1, len(c[0]) - 1):
        m1, m2 = f"{c[i-1][j-1]}{c[i][j]}{c[i+1][j+1]}", f"{c[i+1][j-1]}{c[i][j]}{c[i-1][j+1]}"
        if (m1 == "MAS" or m1[::-1] == "MAS") and (m2 == "MAS" or m2[::-1] == "MAS"):
            s += 1
print(s)
