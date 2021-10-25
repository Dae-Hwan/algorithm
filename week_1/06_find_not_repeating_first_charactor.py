input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for alphabet in string:
        if alphabet.isalpha():
            alphabet_occurrence_array[ord(alphabet) - ord('a')] += 1

        elif not alphabet.isalpha():
            continue

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord('a')))


    for char in string:
        if char in not_repeating_character_array:
            return char


result = find_not_repeating_character(input)
print(result)
