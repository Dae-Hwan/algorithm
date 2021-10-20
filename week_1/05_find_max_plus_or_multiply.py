input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    sum = 0
    # 처음 값이 0이면 더함

    for i in array:
        # 처음 값이 0이면 더함
        # 0,1 이면 더하고
        if i <= 1 or sum <= 0:
            sum += i

        # 0,1이 아니면 곱함
        elif i > 1:
            sum *= i

    return sum


result = find_max_plus_or_multiply(input)
print(result)
