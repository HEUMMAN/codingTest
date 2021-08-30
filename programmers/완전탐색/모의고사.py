def solution(answers):
    answer = [0, 0, 0]
    supo_1 = [1, 2, 3, 4, 5]
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == supo_1[i % 5]:
            answer[0] += 1

        if answers[i] == supo_2[i % 8]:
            answer[1] += 1

        if answers[i] == supo_3[i % 10]:
            answer[2] += 1
    return [i + 1 for i, num in enumerate(answer) if num == max(answer)]