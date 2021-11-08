array = []
for _ in range(19):
    array.append(list(map(int, input().split())))
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    temp = array[x][y]

    for i in range(19):
        if array[x][i] == 0:
            array[x][i] = 1
        else:
            array[x][i] = 0

    for i in range(19):
        if array[i][y] == 0:
            array[i][y] = 1
        else:
            array[i][y] = 0
    array[x][y] = temp


for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end = ' ')
    print('')