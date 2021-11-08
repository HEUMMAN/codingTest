array = []
for _ in range(10):
    array.append(list(map(int, input().split())))

dx = [0, 1]
dy = [1, 0]
x, y = 1, 1

while True:
    array[x][y] = 9
    if array[x + dx[0]][y + dy[0]] == 2:
        array[x + dx[0]][y + dy[0]] = 9
        break
    elif array[x + dx[0]][y + dy[0]] == 0:
        x += dx[0]
        y += dy[0]
    elif array[x + dx[1]][y + dy[1]] == 2:
        array[x + dx[1]][y + dy[1]] = 9
        break
    elif array[x + dx[1]][y + dy[1]] == 0:
        x += dx[1]
        y += dy[1]

    else:
        break


for i in range(len(array)):
    for j in range(len(array[0])):
        print(array[i][j], end = ' ')
    print('')
