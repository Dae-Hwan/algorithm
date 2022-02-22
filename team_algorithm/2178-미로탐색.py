import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline())) for _ in range(N)]
count_graph = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

queue = [[0, 0]]
visited[0][0] = True
count_graph[0][0] = 1

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while queue:
    y, x = queue.pop(0)

    if x == M and y == N:
        break

    for i in range(4):
        nX = x + dx[i]
        nY = y + dy[i]

        if 0 <= nX < M and 0 <= nY < N:
            if graph[nY][nX] == 1 and not visited[nY][nX]:
                visited[nY][nX] = True
                queue.append([nY, nX])
                count_graph[nY][nX] += count_graph[y][x] + 1

print(count_graph[N-1][M-1])

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


