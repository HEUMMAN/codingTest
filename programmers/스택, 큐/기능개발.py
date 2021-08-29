from collections import deque


def solution(progresses, speeds):
    answer = []
    deq = deque(progresses)
    deqs = deque(speeds)
    while len(deq) > 0:
        temp = 0
        for i in range(len(deq)):
            deq[i] += deqs[i]

        if deq[0] >= 100:
            deq.popleft()
            deqs.popleft()
            temp += 1
            for i in range(len(deq)):
                if deq[i] >= 100 and len(deq) > 0:
                    temp += 1
                else:
                    break

            for i in range(temp - 1):
                deq.popleft()
                deqs.popleft()

        if temp > 0:
            answer.append(temp)
    return answer
