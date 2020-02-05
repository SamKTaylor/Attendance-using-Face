#!/bin/python
people = {}
with open("people.txt") as file:
    for line in file:
       (key, val) = line.split()
       people[int(key)] = val

for i in people:
    label=people[i]
    abhi=i
    print(label)
    print(abhi)

