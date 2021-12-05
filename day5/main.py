def day5_2(data,mapList):

    for points in data:
        p1 = list(map(int,points[0]))
        p2 = list(map(int,points[1]))

        if p1[0]!=p2[0] and p1[1]!=p2[1]:

            if p1[0] > p2[0]:
                x1 = p2[0]
                y1 = p2[1]
                x2 = p1[0]
                y2 = p1[1]
            else:
                x1 = p1[0]
                y1 = p1[1]
                x2 = p2[0]
                y2 = p2[1]
            dir = int((y2 - y1) / (x2 - y1))
            for i in range(0,x2 - x1 + 1):
                if str(x1 + i)+','+ str(y1 + i * dir) in mapList.keys():
                    mapList[str(x1 + i)+','+ str(y1 + i * dir)] += 1
                else:
                    mapList[str(x1 + i) + ',' + str(y1 + i * dir)]=1

    return sum([1 for i in mapList.values() if i>1])



def day5_1(data):
    mapList={}

    for points in data:
        p1 = list(map(int,points[0]))
        p2 = list(map(int,points[1]))

        if p1[0]==p2[0]:
            for i in range(min(p1[1],p2[1]), max(p1[1],p2[1])+1):
                if str(p1[0])+','+str(i) in mapList.keys():
                    mapList[str(p1[0])+','+str(i)]+=1
                else:
                    mapList[str(p1[0]) + ',' + str(i)] =1

        if p1[1]==p2[1]:
            for i in range(min(p1[0],p2[0]), max(p1[0],p2[0])+1):
                if str(i) +','+ str(p1[1]) in mapList.keys():
                    mapList[str(i)+','+str(p1[1])]+=1
                else :
                    mapList[str(i) +','+ str(p1[1])] =1

    return sum([1 for i in mapList.values() if i>1]),mapList


if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    data = [(l.split(' -> ')[0].split(','),l.split(' -> ')[1].split(',')) for l in fichier.read().split("\n")]
    res,maplist=day5_1(data)
    print(res)
    print(day5_2(data,maplist))