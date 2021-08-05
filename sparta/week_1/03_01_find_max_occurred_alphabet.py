input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    max_num = 0
    index = 0

    for word in string:
        if word.isalpha():
            alphabet_occurrence_array[ord(word) - ord('a')] += 1

    for i in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[i] > max_num:
            max_num = alphabet_occurrence_array[i]
            index = i

    return chr(97 + index)


result = find_max_occurred_alphabet(input)
print(result)
