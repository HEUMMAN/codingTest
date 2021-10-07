N, M = list(map(int, input().split()))
woods = list(map(int, input().split()))
woods.sort()
answer = woods[0]

for wood in woods:
    left = 0
    right = N + 1

    while True:
        sum = 0
        mid = (left + right) // 2
        for i in range(mid, N):
            sum += woods[i]
        if sum < M:
            left



print(N, M)
print(woods)