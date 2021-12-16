import heapq
import math


def day15_1_1(risks):
    bests = [[math.inf] * len(r) for r in risks]
    bests[0][0] = 0
    queue = []
    heapq.heappush([], (0, 0, 0))
    while True:
        q, x0, y0 = heapq.heappop(queue)
        c = bests[y0][x0]
        if y0 == len(risks) - 1 and x0 == len(risks[y0]) - 1:
            return c
        n = ((x0 - 1, y0), (x0, y0 - 1), (x0, y0 + 1), (x0 + 1, y0))
        for x1, y0 in n:
            if y0 not in range(0,len(risks)) or x1 not in range(0,len(risks[y0])):
                continue
            d = c + risks[y0][x1]
            if d < bests[y0][x1]:
                bests[y0][x1] = d
                heapq.heappush(queue, (d, x1, y0))


def day15_1(data):
    return day15_1_1(data)


def day15_2(data):
    return day15_1_1(data)

if __name__=='__main__':
    fichier = open('input.txt', mode='r')
    data = fichier.read().split("\n")

    print(day15_1([list(map(int, line.strip())) for line in data]))
    data = [[(int(char) - 1 + dx + dy) % 9 + 1 for dx in range(5) for char in line.strip()] for dy in range(5) for line in data ]
    print(day15_2(data))