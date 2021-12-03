import copy
import operator


def day3_1(data):
    length = len(data[0])
    gamma = ''.join(
        ['0' if [i[t] for i in data].count(0) > [i[t] for i in data].count(1) else '1' for t in range(0, length)])
    epsilon = ''.join(
        ['0' if [i[t] for i in data].count(0) < [i[t] for i in data].count(1) else '1' for t in range(0, length)])

    return int(gamma, 2) * int(epsilon, 2)


def day3_2_1(data, op, r):
    if len(data) == 0:
        return int(''.join(r), 2)
    if len(data[0]) == 0:
        return int(''.join(r), 2)

    if len(data) == 1:
        return day3_2_1([], "CO2", r + [str(i) for i in data[0]])

    z = [i[0] for i in data].count(0)
    u = [i[0] for i in data].count(1)
    if op == "O2":
        r.append('1' if u >= z else '0')
        d = [t[1:] for t in data if t[0] == 1 and u >= z or t[0] == 0 and z >= u]
    else:
        r.append('0' if z <= u else '1')

        if len(data) == 2 and u == z:
            if data[0][0] == 0:
                return day3_2_1([], "CO2", r + [str(i) for i in data[0][1:]])
            else:
                return day3_2_1([], "CO2", r + [str(i) for i in data[1][1:]])
        d = [t[1:] for t in data if t[0] == 1 and u < z or t[0] == 0 and z <= u]
    return day3_2_1(d, op, r)


def day3_2(data):
    data2 = copy.deepcopy(data)
    return day3_2_1(data, "O2", []) * day3_2_1(data2, "CO2", [])


if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    data = [[int(i) for i in list(l)] for l in fichier.read().split("\n")]
    print(day3_1(data))
    print(day3_2(data))
