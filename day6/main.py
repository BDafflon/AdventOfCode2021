from copy import deepcopy


def day6_2(data,limit):
    dataDict = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
    for p in data:
        dataDict[str(p)] += 1

    newDict = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
    for day in range(0,limit):
        for day in dataDict:
            if int(day) == 0:
                newDict["6"] += dataDict[day]
                newDict["8"] += dataDict[day]
            else:
                newDict[str(int(day)-1)] += dataDict[day]

        dataDict = deepcopy(newDict)
        newDict = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}

    return sum(dataDict.values())

def day6_1(data,limit):
    for i in range(0,limit):
        cpt = data.count(0)
        data= [ 6 if p==0 else p-1  for p in data]
        data += [8] * cpt
    return len(data)


if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    data = [int(l) for l in fichier.read().split(",")]
    print("1 :",day6_1(data,80))
    print("2 :",day6_2(data, 256))