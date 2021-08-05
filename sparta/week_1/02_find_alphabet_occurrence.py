def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for word in string:
        if word.isalpha():
            alphabet_occurrence_array[ord(word) - ord('a')] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))