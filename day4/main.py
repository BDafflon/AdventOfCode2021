import copy


def day4_1(number, boards, boardsT):
    board = []
    last = 0
    for n in number:
        find = False
        for i in range(0, len(boards)):
            size = len(boards[i])
            sizeTransposed = len(boardsT[i])
            boards[i] = list(filter(lambda x: x, [[ele for ele in sub if ele != n] for sub in boards[i]]))
            boardsT[i] = list(filter(lambda x: x, [[ele for ele in sub if ele != n] for sub in boardsT[i]]))

            if size > len(boards[i]):
                board = [list(map(int, i)) for i in boards[i]]
                last = int(n)
                find = True
                break
            if sizeTransposed > len(boardsT[i]):
                board = [list(map(int, i)) for i in boardsT[i]]
                last = int(n)
                find = True
                break

        if find:
            break

    return sum([sum(i) for i in board]) * last


def day4_2(number, boards, boardsT):
    board = []
    last = 0
    ref = len(boards[0])

    for n in number:
        find = False
        for i in range(0, len(boards)):

            size = len(boards[i])
            sizeTransposed = len(boardsT[i])

            boards[i] = list(filter(lambda x: x, [[ele for ele in sub if ele != n] for sub in boards[i]]))
            boardsT[i] = list(filter(lambda x: x, [[ele for ele in sub if ele != n] for sub in boardsT[i]]))

            if ref - 1 == len(boards[i]) and size > len(boards[i]):
                board = [list(map(int, i)) for i in boards[i]]
                last = int(n)
                boards[i] = []
                boardsT[i] = []

            if ref - 1 == len(boardsT[i]) and sizeTransposed > len(boardsT[i]):
                board = [list(map(int, i)) for i in boardsT[i]]
                last = int(n)
                boards[i] = []
                boardsT[i] = []

    return sum([sum(i) for i in board]) * last


if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    data = [l for l in fichier.read().split("\n\n")]
    number = data[0].split(",")
    boards = [[' '.join(j.split()).split(' ') for j in i.split("\n")] for i in data[1:]]
    boardsT = [[[item[i] for item in boards[j]] for i in range(0, len(boards[j]))] for j in range(0, len(boards))]

    print(day4_1(number, boards, boardsT))
    print(day4_2(number, boards, boardsT))
