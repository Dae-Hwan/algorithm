def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for alphabet in string:
        if alphabet.isalpha():
            alphabet_occurrence_array[ord(alphabet) - ord('a')] += 1

        elif not alphabet.isalpha():
            continue

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))