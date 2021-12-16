
from collections import Counter, defaultdict

def createPolymer(pair_info, pair_counts, element_counts):
    new_polymer = {}
    for pair, total in pair_counts.items():
        element, p1, p2 = pair_info[pair]
        element_counts[element] += total
        if p1 in new_polymer.keys():
            new_polymer[p1] += total
        else:
            new_polymer[p1] = total

        if p2 in new_polymer.keys():
            new_polymer[p2] += total
        else:
            new_polymer[p2] = total
    return new_polymer

def day14_1(polymer,pair_info, iterations):
    pair_nb =Counter(''.join(pair) for pair in zip(polymer, polymer[1:]))
    element_counts = Counter(polymer)
    for i in range(0,iterations):
        pair_nb = createPolymer(pair_info, pair_nb, element_counts)
    totals = sorted(element_counts.values())
    return totals[-1] - totals[0]



if __name__=='__main__':
    fichier = open('input.txt', mode='r')
    polymer, insertion_rules = fichier.read().split('\n\n')
    pair_info = {}
    for char1, char2, *_, element in insertion_rules.split('\n'):
        pair_info[char1 + char2] = (element, char1 + element, element + char2)

    print(day14_1(polymer,pair_info,10))
    print(day14_1(polymer,pair_info,40))