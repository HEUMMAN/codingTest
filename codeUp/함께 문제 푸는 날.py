a, b, c = map(int, input().split())
day = 1
while True:
    day += 1
    if day % a == 0:
        if day % b == 0:
            if day % c == 0:
                print(day)
                break
