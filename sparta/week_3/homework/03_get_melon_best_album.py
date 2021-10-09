genres = ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"]
plays = [2000, 500, 600, 150, 800, 2500, 2000]


def get_melon_best_album(genre_array, play_array):
    melon_dict = {}
    rank_dict = {}
    dict_arr = []
    result = []

    for i in range(len(genre_array)):
        key, value = genre_array[i], play_array[i]
        if key not in dict_arr:
            dict_arr.append(key)
            melon_dict[key] = [i, value]
        else:
            melon_dict[key] = melon_dict[key] + [i, value]

    sum_genre = [0]*len(dict_arr)
    for i in range(len(dict_arr)):
        for j in range(len(melon_dict[dict_arr[i]])):
            if j % 2 != 0:
                sum_genre[i] += melon_dict[dict_arr[i]][j]

    for i in range(len(dict_arr)):
        rank_dict[dict_arr[i]] = sum_genre[i]
    rank_dict = sorted(rank_dict.items(), key=lambda x: x[1], reverse=True)

    for i in range(len(dict_arr)):
        for _ in range(2):
            genre = rank_dict[i][0]
            index = max(melon_dict[genre])
            for j in range(len(melon_dict[genre])):
                if melon_dict[genre][j] == index:
                    result.append(melon_dict[genre][j-1])
                    melon_dict[genre][j] = -1
                    break

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
