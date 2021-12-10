def day10_2(data,scoreDict,caraDict):
    stack = []
    for c in data:
        if (c in scoreDict):
            stack.append(c)
        else:
            top = stack.pop() if stack else None
            if (top != caraDict[c]):
                return 0

    score = 0
    for ch in reversed(stack):
        score *= 5
        score += scoreDict[ch]

    return score

def day10_1(data,scoreDict,caraDict):
    stack = []
    for d in data:
        if (d in '([{<'):
            stack.append(d)
        else:
            top = stack.pop() if stack else None
            if (top != caraDict[d]):
                return scoreDict[d]
    return 0


if __name__ == '__main__':
    fichier = open('input.txt', 'r')

    caraDict = {')': '(', ']': '[', '}': '{', '>': '<'}
    data = fichier.read().split("\n")

    scoreDict = {')': 3, ']': 57, '}': 1197, '>': 25137}
    print(sum([ day10_1(i,scoreDict,caraDict) for i in data]))

    scoreDict = {'(': 1, '[': 2, '{': 3, '<': 4}
    print(sorted([ day10_2(i, scoreDict, caraDict) for i in data  if day10_2(i, scoreDict, caraDict) != 0])[int(len([ day10_2(i, scoreDict, caraDict) for i in data  if day10_2(i, scoreDict, caraDict) != 0])/2)])
