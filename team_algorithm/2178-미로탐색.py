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
def bfs(x, y, n, m):
    count = 0

    queue = deque()
    queue.append((y, x))

    while queue:
        if x == n and y == m:
            return count

        y, x = queue.popleft()
        # 오른쪽
        if maze[y][x + 1] == 1:
            count += 1
            print("right", count)
            queue.append((y, x + 1))

        # 위로
        if maze[y + 1][x] == 1:
            count += 1
            print("down", count)
            queue.append((y + 1, x))

        # 왼쪽
        if maze[y][x - 1]:
            count += 1
            print("left", count)
            queue.append((y, x - 1))

        # 아래로
        if maze[y - 1][x]:
            count += 1
            print("up", count)
            queue.append((y - 1, x))

        maze[y][x] = 0

    return count


bfs(1, 1, n + 1, m + 1)


# 실수 -> 거리탐색인데 dfs로 풀라했다.
