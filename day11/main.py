def step(m):
  # 1
  for (x,y) in m.keys():
    m[(x,y)]+=1
  # 2
  flash = set()
  newflash = {(x,y) for (x,y),v in m.items() if v>9}
  while len(newflash)>0:
    flash = spread(m,flash,newflash)
    newflash = {(x,y) for (x,y),v in m.items() if v>9 and (x,y) not in flash}
  # 3
  for x,y in flash:
    m[(x,y)]=0
  return len(flash)

def neighbours(x,y,mx,my):
  return [(x+dx,y+dy) for dx in (-1,0,1) for dy in (-1,0,1)
      if x+dx>=0 and y+dy>=0 and x+dx<=mx and y+dy<=my and not (dx==0 and dy==0)]


def spread(m,flash,newflash):
  flash = flash.union(newflash)
  for x,y in newflash:
    for xx,yy in neighbours(x, y, maxX, maxY):
      if (xx,yy) not in flash:
        m[(xx,yy)]+=1
  return flash


def day11_1(map):
    n = 0
    for i in range(0, 100):
        n += step(map)
    return n


def day11_2(map):
    for i in range(100, 999):
        k = step(map)
        if k == (maxX + 1) * (maxY + 1):
            return (i + 1)
            break


if __name__=='__main__':
    map={(x, y):int(c) for x, l in enumerate(open("input.txt", "rt")) for y, c in enumerate(l.strip())}
    maxX=max(x for x, y in map.keys())
    maxY=max(y for x, y in map.keys())

    print(day11_1(map))
    print(day11_2(map))





