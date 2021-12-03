def day1_1(data):
    return sum([data[i - 1] < x if i < len(data) else 0 for i, x in enumerate(data)][1:])


def day1_2(data):
    return day1_1([sum(data[i:i + 3]) for i, v in enumerate(data) if len(data[i:i + 3]) == 3])


if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    data = [int(l.rstrip()) for l in fichier.read().split("\n")]
    print(day1_1(data))
    print(day1_2(data))
