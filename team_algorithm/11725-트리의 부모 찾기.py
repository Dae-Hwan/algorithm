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
                visited[i] = True

N = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
result = [[] for _ in range(N + 1)]

# 중력이 생기기전
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# for n in range(1, N + 1):
bfs(1)
print(result)