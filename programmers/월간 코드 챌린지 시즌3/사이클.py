def solution(grid):
    grid_dic = {}
    answer = []
    garo = 0
    sero = 0
    now_direction = ['Down', 'Up', 'Right', 'Left']
    count = 0
    real_answer = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid_dic[str(i) + str(j)] = ''

    for i in range(len(now_direction)):
        answer.append(check_cycle(count, garo, grid, now_direction[i], sero, grid_dic))

    for i in range(len(answer)):
        if answer[i] is not None:
            real_answer.append(answer[i])
    real_answer = sorted(real_answer, reverse=True)
    return real_answer


def check_cycle(count, garo, grid, now_direction, sero, grid_dic):
    count = 0
    while True:
        if grid[garo][sero] == 'S':
            pass

        elif grid[garo][sero] == 'L':
            if now_direction == 'Down':
                now_direction = 'Right'
            elif now_direction == 'Right':
                now_direction = 'Up'
            elif now_direction == 'Up':
                now_direction = 'Left'
            else:
                now_direction = 'Down'

        else:
            if now_direction == 'Down':
                now_direction = 'Left'
            elif now_direction == 'Right':
                now_direction = 'Down'
            elif now_direction == 'Up':
                now_direction = 'Right'
            else:
                now_direction = 'Up'

        if now_direction == 'Down':
            sero += 1
            if sero > len(grid[0]) - 1:
                sero = 0

        elif now_direction == 'Up':
            sero -= 1
            if sero < 0:
                sero = len(grid[0]) - 1

        elif now_direction == 'Right':
            garo += 1
            if garo > len(grid) - 1:
                garo = 0
        else:
            garo -= 1
            if garo < 0:
                garo = len(grid) - 1

        if count == 0:
            start = [now_direction, garo, sero]

        else:
            if [now_direction, garo, sero] == start:
                return count
        if now_direction in grid_dic[str(garo) + str(sero)]:
            break
        grid_dic[str(garo) + str(sero)] = grid_dic[str(garo) + str(sero)] + str(' ') + now_direction
        count += 1

print(solution(["LRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLR","RLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRL"]))
