import numpy as np


def day2_1(data,f=0,p=0):
    return np.sum(data,0)[0]+f * np.sum(data,0)[1]+p

def day2_2(data,f=0,p=0):
    print(data)
    position = [f,p]
    aim = 0
    for d in data:
        if d[1]!=0:
            aim+=d[1]
        if d[0]!=0:
            position[0]+=d[0]
            position[1]+=aim*d[0]
    return position[0]*position[1]


def replace(d):
    d[1]=int(d[1])
    if d[0]=="forward":
        return [d[1],0]
    if d[0] == "down":
        return [0,d[1]]
    if d[0] == "up":
        return [0,-d[1]]


if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    data = [  replace(l.rstrip().split(' ')) for l in fichier.read().split("\n")]

    print(day2_1(data))
    print(day2_2(data))