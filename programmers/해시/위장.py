def solution(clothes):
    types = []
    for cloth, type_ in clothes:
        types.append(type_)
    sets = set(types)
    answer = [0] * len(sets)

    for i in range(len(sets)):
        for j in range(len(types)):
            if sets[i] == types[j]:
                answer[i] += 1
    print(answer)

    return answer
solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])