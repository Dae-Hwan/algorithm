def solution(clothes):
    dict = {}
    for i in clothes:
        dict[i[1]] = dict.get(i[1], 1) + 1

    print(dict)

    if len(dict) == 0:
        return 0

    elif len(dict) == 1:
        for v in dict.values():
            return v - 1

    else:
        multiply = 1
        for v in dict.values():
            multiply *= v

        return multiply - 1