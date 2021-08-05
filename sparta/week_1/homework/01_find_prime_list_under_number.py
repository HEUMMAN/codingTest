input = 20


def find_prime_list_under_number(number):
    array = []
    flag = 0
    if number < 2:
        return '_'

    for i in range(2, number+1):
        for j in range(2, i):
            if i <= 2:
                continue
            else:
                if i % j == 0:
                    flag = 1
                    break
                else:
                    continue

        if flag == 0:
            array.append(i)
        flag = 0
    return array


result = find_prime_list_under_number(input)
print(result)
