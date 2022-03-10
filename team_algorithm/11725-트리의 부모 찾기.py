import sys
from collections import deque


def bfs(n):
    visited[n] = True
    queue = deque()
    queue.append(n)

    while queue:
        queue_n = queue.popleft()

        for i in graph[queue_n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = queue_n


N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

# 중력이 생기기전
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
for i in range(len(visited)):
    if i >= 2:
        print(visited[i])