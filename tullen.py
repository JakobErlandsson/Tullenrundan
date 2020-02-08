from itertools import permutations
from numpy import loadtxt, delete
M = loadtxt(open("kollektiv.csv", "rb"), delimiter=",", skiprows=1, usecols=tuple(range(1,9)))
locations = ["Mölndal", "Johanneberg", "Avenyn", "Majorna", "Kville", "Svingeln", "Kålltorp", "Andra Lång"]
indices = list(range(len(locations)))

for j in indices:
    print(locations[j] + ":")
    shortest = 10000
    best = []
    perms = list(permutations([x for x in indices if x != j]))
    for p in perms:
        s = M[j][p[0]]
        for i in range(len(p)-1):
            s += M[p[i]][p[i+1]]
        if s < shortest:
            shortest = s
            best = p
    loc = [locations[k] for k in best]
    print(loc, str(int(shortest))+"min\n")

