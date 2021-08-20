import heapq

ramen_stock = 2
supply_dates = [1, 10]
supply_supplies = [10, 100]
supply_recover_k = 11


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    dic = {}
    for i in range(len(dates)):
        dic[dates[i]] = supplies[i]
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    cur_supply = ramen_stock
    date_index = 0
    cnt = 0
    visited = []
    while cur_supply <= k:
        if cur_supply >= dic[date_index][0] and dic[date_index][0] not in visited:
            cur_supply += dic[date_index][1]
            visited.append(dic[date_index][0])
            cnt += 1
        date_index += 1
    return cnt


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))


'''
import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    last_added_date_index = 0
    max_heap = []

    while stock <= k:
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
            heapq.heappush(max_heap, -supplies[last_added_date_index])
            last_added_date_index += 1

        **answer += 1
        heappop = heapq.heappop(max_heap)
        stock += -heappop**

    return answer

print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))
'''