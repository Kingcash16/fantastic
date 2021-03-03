# Joshua Jaja ID:1543343 Zylab 8.10:

import csv

FN = input()

WF = {}

with open(FN, 'r') as cfile:
    creader = csv.reader(cfile)
    for row in creader:
        for word in row:
            if word not in WF.keys():
                WF[word] = 1
            else:
                WF[word] += 1
for key in WF.keys():
    print(key + " " + str(WF[key]))