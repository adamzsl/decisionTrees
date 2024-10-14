import csv
import math

peopleList = []
survived = []

def mapAge(age):
    if age<=20:
        return ("young")
    if age <=40:
        return ("middle")
    return ("old")

def calculateEntropy(d):
    all = sum(d.values())
    prob = [i/all for i in d.values()]
    return -sum([p*math.log2(p) for p in prob])

def getDict(l):
    d = {}
    for el in l:
        d[el] = d.get(el,0) + 1
    return d


with open("titanic-homework.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    for row in reader:
        peopleList.append([row[1]]+[row[3]]+[mapAge(int(row[4]))]+row[5:])
        survived.append(int(row[7]))

entropy = calculateEntropy(getDict(survived))
    
entropyList = []
for col in range(len(peopleList[0])):
    d = {}
    for index,row in enumerate(peopleList):
        d[row[col]] = d.get(row[col][0],0) + 1

    print(d)
    break


print(peopleList[0])
print(entropy)

