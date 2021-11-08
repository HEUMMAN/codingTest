n = int(input())
number = [0 for _ in range(23)]
array = list(map(int, input().split()))

for i in range(len(array)):
    number[array[i]-1] += 1

for i in range(len(number)):
    print(number[i], end = ' ')