def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visited = []
    visited.append((begin, 0))
    while visited:
        now, depth = visited.pop(0)
        for word in words:
            diff = 0
            for i in range(len(word)):
                if now[i] != word[i]:
                    diff += 1
            if diff == 1 and word == target:
                depth += 1
                return depth
            elif diff == 1:
                visited.append((word, depth + 1))
    return answer

