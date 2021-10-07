n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
M = list(map(int, input().split()))

for i in range(m):
    left = 0
    right = n - 1
    target = M[i]
    is_find = False

    while True:
        mid = (left + right) // 2
        if target == A[mid]:
            print(1)
            is_find = True
            break
        elif target > A[mid]:
            left = mid + 1
        elif target < A[mid]:
            right = mid - 1

        if left > right:
            break
    if not is_find:
        print(0)
