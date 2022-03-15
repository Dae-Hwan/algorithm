def solution(participant, completion):
    dict = {}
    for p in participant:
        dict[p] = dict.get(p, 0) + 1
    print(dict)

    for c in completion:
        if c in dict:
            dict[c] = dict.get(c) - 1

    for i in dict:
        if dict[i] == 1:
            return i