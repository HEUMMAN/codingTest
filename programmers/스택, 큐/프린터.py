def solution(priorities, location):
    pointer = 0
    arr = []

    while priorities:
        max_priorities = max(priorities)
        now = priorities.pop(0)

        if now == max_priorities:  # 맨 앞 원소가 최대 원소일 경우
            arr.append(now)  # arr 맨 뒤에 추가함(인쇄 됨)
            if pointer == location:  # 그 원소가 요청한 문서일 경우
                return len(arr)  # 몇 번째로 인쇄되었는지 판단

        else:
            priorities.append(now)  # 맨 앞 원소가 최대 원소가 아닐 경우
            if pointer == location:  # 그 원소가 요청한 문서일 경우
                location = len(priorities)  # 맨 뒤로 위치 변경

        pointer += 1
        