current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    #0:북, 1:동, 2:남, 3:서
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    cnt = 1
    room_map[r][c] = -1
    queue = [[r, c, d]]

    while queue:
        r, c, d = queue.pop(0)
        temp_d = d

        for i in range(4):
            temp_d = (temp_d + 3) % 4
            new_r, new_c = r + dy[temp_d], c + dx[temp_d]

            if 0 <= new_r < len(room_map) and 0 <= new_c < len(room_map[0]) and room_map[new_r][new_c] == 0:
                cnt += 1
                room_map[new_r][new_c] = -1
                queue.append([new_r, new_c, temp_d])
                break

            elif i == 3:
                new_r, new_c = r + dy[(d + 2) % 4], c + dx[(d + 2) % 4]
                queue.append([new_r, new_c, d])

                if room_map[new_r][new_c] == 1:
                    return cnt

# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))