def solution(N, number):
    dp = []

    li = [set() for i in range(8)]

    if number == N:
        return 1

    for i in range(len(li)):
        li[i].add(int(str(N) * (i + 1)))

    for i in range(1, 8):
        for j in range(i):  # 0  0,1  0,1,2
            for op1 in li[j]:
                for op2 in li[i - j - 1]:
                    li[i].add(op1 + op2)
                    li[i].add(op1 - op2)
                    li[i].add(op1 * op2)
                    if op2 != 0:
                        li[i].add(op1 // op2)
        if number in li[i]:
            return i + 1

    return -1