from itertools import permutations


def get_prime_number(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def solution(numbers):
    answer = []
    for i in range(1, len(numbers) + 1):
        arr = list(permutations(numbers, i))
        for j in range(len(arr)):
            num = int(''.join(map(str, arr[j])))
            if get_prime_number(num):
                answer.append(num)

    answer = list(set(answer))
    return len(answer)
