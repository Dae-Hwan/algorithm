input = "abacabade"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for alphabet in string:
        if alphabet.isalpha():
            alphabet_occurrence_array[ord(alphabet) - ord('a')] += 1

        elif not alphabet.isalpha():
            continue
    return alphabet_occurrence_array

    # for index in range(len(alphabet_occurrence_array)):
    #     if alphabet_occurrence_array[index] == 1:
    #         print(alphabet_occurrence_array[index])
        # if i == 1:
        #     print(chr(alphabet_occurrence_array[i] + ord('a')))

    # for str in string:

    # str이
    # 같은 값이 있으면 break
    # 같은 값이없다면 리턴



result = find_not_repeating_character(input)
print(result)