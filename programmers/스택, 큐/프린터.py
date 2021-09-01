def solution(priorities, location):
    answer = 0

    while priorities:
        max_priorities = max(priorities) #배열 중 최대 원소 저장
        now = priorities.pop(0) #맨 앞 원소 추출

        if now == max_priorities:  #맨 앞 원소가 최대 원소일 경우
            answer += 1 #인쇄 된 수 + 1
            if location == 0: #맨 앞 원소가 최대 원소이며, 요청한 문서인 경우
                break
            else: #맨 앞 원소가 최대 원소이지만, 요청한 문서가 아닌 경우
                location -= 1 #요청한 문서의 위치 -1
        else: #맨 앞 원소가 최대 원소가 아닐 경우
            priorities.append(now) #맨 뒤에 원소 추가
            if location == 0: #맨 앞 원소가 최대 원소가 아니지만, 요청한 문서인 경우
                location = len(priorities)-1 #요청한 문서의 위치는 맨 뒤
            else: #맨 앞 원소가 최대 원소가 아니며, 요청한 문서도 아닌 경우
                location -= 1 #요청한 문서의 위치 -1
    return answer
