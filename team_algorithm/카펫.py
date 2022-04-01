def solution(brown, yellow):  # 10 2
    plus = brown + yellow  # 12 12*1 6*2 4*3
    plus_list = []  # 약수 리스트

    for i in range(1, plus + 1):
        # 나누어 떨어지면
        if plus % i == 0:
            plus_list.append(i)

    print(plus_list)
    tuple_list = []  # 곱셈 짝궁 리스트
    # 짝수
    if len(plus_list) % 2 == 0:
        for _ in range(len(plus_list) // 2):
            tuple_list.append((plus_list.pop(), plus_list.pop(0)))

    # 짝수
    if len(plus_list) % 2 != 0:
        for i in range((len(plus_list) // 2) + 1):
            if i == (len(plus_list) // 2) + 1:
                x = plus_list.pop()
                tuple_list.append((x, x))
            else:
                tuple_list.append((plus_list.pop(), plus_list.pop(0)))

    print(tuple_list)
    for a, b in tuple_list:
        if (a - 2) * (b - 2) == yellow:
            return [a, b]