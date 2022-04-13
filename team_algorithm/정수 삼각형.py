def solution(triangle):
    for a in range(1, len(triangle)):  # a = 줄 인덱스
        for b in range(len(triangle[a])):  # b = 값 인덱스
            if b == 0:
                triangle[a][b] += triangle[a - 1][b]
            elif b == len(triangle[a]) - 1:
                triangle[a][b] += triangle[a - 1][b - 1]
            else:
                triangle[a][b] += max(triangle[a - 1][b], triangle[a - 1][b - 1])

    return max(triangle[-1])