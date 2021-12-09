import math
from functools import reduce


def voisin(h, w,mH,mW):
    voisins = [ (h+1, w), (h-1, w), (h, w-1), (h, w+1)]
    return list(filter(lambda x: 0 <= x[0] < mH and 0 <= x[1] < mW, voisins))


def day9_2(data):
    points = [(h,w) for h in range(0, len(data)) for w in range(0, len(data[0])) if data[h][w] < min([data[j][i] for j, i in voisin(h, w, len(data), len(data[0]))])]
    return reduce((lambda x, y: x * y), sorted([day9_2_1(data,p, []) for p in points])[-3:])


def day9_2_1(data,lowPoint,points):
        if points is None:
            points = []

        voisins = [(j,i) for j, i in voisin(lowPoint[0], lowPoint[1], len(data), len(data[0]))]
        cpt = 0

        for n in voisins:
            if n not in points and data[n[0]][n[1]] != 9:
                points.append(n)
                cpt += 1 + day9_2_1(data, n, points)

        return cpt

def day9_1(data):
    res = [data[h][w]+1 for h in range(0, len(data)) for w in range(0, len(data[0])) if data[h][w] < min([data[j][i] for j, i in voisin(h, w, len(data), len(data[0]))])]
    return sum(res)

if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    data =  [list(map(int,x.split('\n')[0])) for x in fichier.readlines()]
    print(day9_1(data))
    print(day9_2(data))

