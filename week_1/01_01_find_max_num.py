input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num = array[0]
    for now_num in array:
        if max_num <= now_num:
            max_num = now_num

        elif now_num > max_num:
            continue

    return max_num


result = find_max_num(input)
print(result)
