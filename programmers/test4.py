def solution(n, info):
    target = 0
    ryan_info = [0] * 11
    answer = []
    dfs(n, target, info, ryan_info, answer)
    print(answer)
    print(len(answer))
    return answer


def dfs(n, target, info, ryan_info, answer):
    if sum(ryan_info) > 5:
        return
    if n == 0:
        ryan_sum = 0
        apeach_sum = 0
        for i in range(len(info)):
            if ryan_info[i] - info[i] > 0:
                ryan_sum += (10-i)
            elif ryan_info[i] == info[i] == 0:
                ryan_sum += 0
                apeach_sum += 0
            else:
                apeach_sum += (10-i)
        if ryan_sum > apeach_sum:
            answer.append(ryan_info)
            return

    else:
        for i in range(n):
            target -= i
            ryan_info[target] += 1
            dfs(n-1, target, info, ryan_info, answer)

solution(5, [2,1,1,1,0,0,0,0,0,0,0])
#solution(10, [0,0,0,0,0,0,0,0,3,4,3])