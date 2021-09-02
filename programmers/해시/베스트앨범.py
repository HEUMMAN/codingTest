def solution(genres, plays):
    answer = []
    best_album = []
    dic = {}

    # 딕셔너리에 장르들 중복 안되게 추가
    for genre in genres:
        if genre not in dic:
            dic[genre] = 0

    # 장르 별 곡 숫자 합산
    for i in range(len(plays)):
        dic[genres[i]] += plays[i]

    # 노래가 많이 재생된 장르별로 정렬
    dic = sorted(dic.items(), reverse=True)
    for i in range(len(dic)):
        best_album.append(dic[i][0])

    # 노래가 많이 재생된 장르별로 곡들 수록
    for i in range(len(best_album)):
        temp = []
        for j in range(len(genres)):
            if genres[j] == best_album[i]:
                temp.append(plays[j])

        print(temp)
        max_song = max(temp)
        max_song_index = temp.index(max_song)
        value = temp.pop(max_song_index)

        for k in range(len(genres)):
            if genres[k] == best_album[i] and plays[k] == value:
                answer.append(k)
                break

        if len(temp) < 1:
            continue
        else:
            max_song = max(temp)
            max_song_index = temp.index(max_song)
            value = temp.pop(max_song_index)

            for k in range(len(genres)):
                if genres[k] == best_album[i] and plays[k] == value:
                    answer.append(k)
                    break

    return answer

#print(solution(["classic", "pop", "classic", "classic","jazz","pop", "Rock", "jazz"] ,[500, 600, 150, 800, 1100, 2500, 100, 1000]))
print(solution(["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"],  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))