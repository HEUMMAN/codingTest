array = [[0 for _ in range(19)] for _ in range(19)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    array[x][y] = 1

for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end = ' ')
    print('')
