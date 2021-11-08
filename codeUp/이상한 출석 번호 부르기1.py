n = int(input())
array = list(map(int, input().split()))

for i in range(len(array)):
    print(array[-i-1], end = ' ')