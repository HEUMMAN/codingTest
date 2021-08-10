seat_count = 11
vip_seat_array = [2 ,5]
fibo_memo = {
    1: 1,
    2: 2
}


def fibo(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    fibo_memo[n] = fibo(n-1, fibo_memo) + fibo(n-2, fibo_memo)
    return fibo_memo[n]


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    result = []
    end = 0
    for i in range(1, seat_count+1):
        end += 1
        if i in vip_seat_array:
            result.append(end-1)
            end = 0

        elif i == seat_count:
            result.append(end)
            end = 0
    answer = 1
    for i in range(len(result)):
        answer *= fibo(result[i], fibo_memo)

    print(result)
    return answer


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))