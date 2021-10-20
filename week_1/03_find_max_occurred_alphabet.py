input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for alphabet in string:
        if alphabet.isalpha():
            alphabet_occurrence_array[ord(alphabet) - ord('a')] += 1

        elif not alphabet.isalpha():
            continue

    alphabet_index_list = []
    alphabet_index = 0
    max_occur = 0
    for alphabet_occur in alphabet_occurrence_array:
        if max_occur < alphabet_occur:
            max_occur = alphabet_occur
            alphabet_index_list = []
            alphabet_index_list.append(alphabet_index)

        elif max_occur == alphabet_occur:
            alphabet_index_list.append(alphabet_index)

        alphabet_index += 1

    alphabet_list = []
    for alphabet_index in alphabet_index_list:
        alphabet_list.append(chr(alphabet_index + ord('a')))

    return alphabet_list


result = find_max_occurred_alphabet(input)
print(result)
