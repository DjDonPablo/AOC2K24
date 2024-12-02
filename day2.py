import numpy as np

with open("input.txt") as f:
    c = f.readlines()
# part 1
f=lambda e: len(e) == len(e[(e >= 1) & (e <= 3)])
print(sum([f(abs(e)) if (len(e[e < 0]) == 0 or len(e[e < 0]) == len(e)) else 0 for e in [np.diff(np.array(list(map(int, l.split())))) for l in c]]))

# part 2
def g(e):
    d = np.diff(e)
    if (len(d[d < 0]) == 0 or len(d[d < 0]) == len(d)) and f(d):
        return True
    return any([f(abs(e)) if (len(e[e < 0]) == 0 or len(e[e < 0]) == len(e)) else 0 for e in [np.diff(np.concatenate((e[:i], e[i+1:]))) for i in range(len(e))]])

print(sum([g(e) for e in [np.array(list(map(int, l.split()))) for l in c]]))
