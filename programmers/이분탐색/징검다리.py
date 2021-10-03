def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    answer = 0

    while left <= right:
        prev = 0
        mins = 1000000000
        removed_rocks = 0
        mid = (left + right) // 2

        for i in range(len(rocks)):
            min_rock_distance = rocks[i] - prev
            if min_rock_distance < mid:
                if i != len(rocks) - 1:
                    removed_rocks += 1
            else:
                mins = min(mins, min_rock_distance)
                prev = rocks[i]
            if removed_rocks > n:
                right = mid - 1
            else:
                answer = mins
                left = mid + 1
    return answer


