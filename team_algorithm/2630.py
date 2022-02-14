import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []


def devide(x, y, N):
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                devide(x, y, N // 2)
                devide(x, y + N // 2, N // 2)
                devide(x + N // 2, y, N // 2)
                devide(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        result.append(0)
    elif color == 1:
        result.append(1)

devide(0, 0, N)
print(result.count(0))
print(result.count(1))