import time

start = time.time()


def find_max_occurred_one_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for alphabet in string:
        if alphabet.isalpha():
            big_letter = alphabet.upper()
            alphabet_occurrence_array[ord(big_letter) - ord('A')] += 1

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
        alphabet_list.append(chr(alphabet_index + ord('A')))

    if len(alphabet_list) == 1:
        return alphabet_list[0]
    else:
        return '???'


print(find_max_occurred_one_alphabet('baaa'))

print(time.time() - start)


#################################
#################################
#################################
words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words:
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1:  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])

print(time.time() - start)

