import numpy as np
import re
from copy import deepcopy,copy

print('Day 13 of Advent of Code!')


def parse_data(data):
    raw_points, raw_instructions = data.split('\n\n')
    regex = r'fold along (\w+)=(\d+)'
    points = {tuple(map(int, raw_point.split(','))): 1 for raw_point in raw_points.splitlines()}
    instructions = list()

    for raw_instruction in raw_instructions.splitlines():
        instruction = re.findall(regex, raw_instruction)[0]
        instructions.append((instruction[0], int(instruction[1])))

    return points, instructions


def fold(points, axis, line):
    new_points = copy(points)
    for point in points:
        x, y = point[0], point[1]
        new_point = None
        if axis == 'x' and x > line:
            new_point = (x - 2 * (x - line), y)
        elif axis == 'y' and y > line:
            new_point = (x, y - 2 * (y - line))
        if new_point:
            new_points[new_point] = 1
            new_points.pop(point, None)
    return new_points


def day13_2(points,instructions):
    for i, instruction in enumerate(instructions):
        axis, line = instruction[0], instruction[1]
        points = fold(points, axis, line)

    height = max(pt[0] for pt in points) + 1
    width = max(pt[1] for pt in points) + 1
    paper = np.zeros((width, height))
    for point in points.keys():
        y, x = point[0], point[1]
        paper[x][y] = 1
    for line in paper:
        print(''.join(['*' if char == 1 else ' ' for char in line]))


def day13_1(points, instructions):
    for i, instruction in enumerate(instructions):
        axis, line = instruction[0], instruction[1]
        points = fold(points, axis, line)
        if i == 0:
            return len(points)



if __name__=='__main__':
    fichier = open('input.txt', mode='r')
    data = fichier.read()
    points, instructions = parse_data(data)
    print(day13_1(deepcopy(points), instructions))
    day13_2(points, instructions)