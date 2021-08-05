n = int(input())
words = [[] for _ in range(n)]
cnt = n

for i in range(n):
    word = input()
    for alphabet in word:
        words[i].append(alphabet)

for i in range(len(words)):
    if len(words[i]) == 1:
        continue
    else:
        check = []
        check.append(words[i][0])
        for j in range(len(words[i])-1):
            if words[i][j+1] not in check:
                check.append(words[i][j])
            elif words[i][j] == words[i][j+1]:
                continue
            else:
                cnt -= 1
                break
print(cnt)