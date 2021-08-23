import heapq

def solution(scoville, K):
    heap = []
    for index in scoville:
        heapq.heappush(heap, index)

    answer = 0

    while heap[0] < K:
        if len(heap) <= 2:
            if heap[0] + heap[1] * 2 < K:
                return -1

        heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        answer += 1
    return answer