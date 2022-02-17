import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
print(paper)

check = -1

for x in range(0, N, N // 2):
    for y in range(0, N, N // 2):
        color = paper[x][y]
        # print(x, y)
        print(color)
        if color != paper[]

# 가장 왼쪽 우측거만 계산하자


