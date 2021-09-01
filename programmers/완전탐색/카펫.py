def solution(brown, yellow):
    sum_ = brown + yellow
    for garo in range(sum_, 2, -1):
        if sum_ % garo == 0:
            sero = sum_ // garo
            if yellow == (garo-2) * (sero-2):
                return [garo, sero]
