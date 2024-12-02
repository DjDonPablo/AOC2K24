with open("input.txt") as f:
    c = f.readlines()
# part 1
f=lambda x: zip(sorted(x[0]), sorted(x[1]))
print(sum([abs(int(e[0]) - int(e[1])) for e in f(list(zip(*[l.split() for l in c])))]))

# part 2
l1,l2=list(zip(*[l.split() for l in c]))
print(sum([int(l1[i])*l2.count(l1[i]) for i in range(len(l1))]))
