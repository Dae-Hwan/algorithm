import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = []
for i in range(n + 2):
    if i == 0:
        maze.append([0] * (m + 2))

    elif i == (n + 1):
        maze.append([0] * (m + 2))

    else:
        maze.append([0] + list(map(int, sys.stdin.readline().strip())) + [0])


# 너비 우선 탐색
def bfs(x, y):
    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # deque 생성
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 벽이므로 진행 불가
            if maze[nx][ny] == 0:
                continue

            # 벽이 아니므로 이동
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                print(nx, ny)
                queue.append((nx, ny))

    # 마지막 값에서 카운트 값을 뽑는다.
    return maze[n][m]


print(bfs(1, 1))

# n, m = map(int, sys.stdin.readline().split())
# maze = []
# for i in range(n + 2):
#     if i == 0:
#         maze.append([0] * (m + 2))
#
#     elif i == (n + 1):
#         maze.append([0] * (m + 2))
#
#     else:
#         maze.append([0] + list(map(int, sys.stdin.readline().strip())) + [0])
#
#
#
# # 너비 우선 탐색
# def bfs(x, y, n, m):
#     count = 0
#
#     queue = deque()
#     queue.append((y, x))
#
#     while queue:
#         if x == n and y == m:
#             return count
#
#         y, x = queue.popleft()
#         # 오른쪽
#         if maze[y][x + 1] == 1:
#             count += 1
#             print("right", count)
#             queue.append((y, x + 1))
#
#         # 위로
#         if maze[y + 1][x] == 1:
#             count += 1
#             print("down", count)
#             queue.append((y + 1, x))
#
#         # 왼쪽
#         if maze[y][x - 1]:
#             count += 1
#             print("left", count)
#             queue.append((y, x - 1))
#
#         # 아래로
#         if maze[y - 1][x]:
#             count += 1
#             print("up", count)
#             queue.append((y - 1, x))
#
#         maze[y][x] = 0
#
#     return count
#
#
# bfs(1, 1, n + 1, m + 1)


