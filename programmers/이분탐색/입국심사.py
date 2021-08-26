def solution(n, times):
    times.sort()
    left = 0
    right = times[-1] * n
    while left < right:
        mid = (left + right) // 2
        temp = 0
        for time in times:
            temp += mid // time
        if temp >= n:
            right = mid
        else:
            left = mid + 1
    return right
