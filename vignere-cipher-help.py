
from collections import Counter

string="E wirxirgi mw xli fewmg yrmx sj perkyeki almgl ibtviwwiw e gsqtpixi xlsyklx Mx hsiw xlmw fc jsppsamrk xli kveqqexmgep fewmg vypiw sj wcrxeb"
total = 0

for i in string:
     total += 1

totalfreq = 0
for x in range(25):
    newStr = ""
    totalfreq = 0
    for c in string:
        newStr = newStr + chr((((ord(c) - 97) + x) % 26) + 97)
    counts=Counter(newStr)
    for char in counts:
        totalfreq += (counts[char]/total) * (counts[char]/total)
    print(newStr)
