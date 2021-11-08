h, w = map(int, input().split())
n = int(input())
array = [[0] * w for _ in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())
    x -= 1
    y -= 1

    if d == 0:
        for _ in range(l):
            array[x][y] = 1
            y += 1

    elif d == 1:
        for _ in range(l):
            array[x][y] = 1
            x += 1

for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end = ' ')
    print('')