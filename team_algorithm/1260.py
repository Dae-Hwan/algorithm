import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)  # 정점의 숫자 + 1만큼 만듬

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a) # graph [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]


# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
for i in range(1, n+1):
    graph[i].sort()


# 깊이 우선 탐색
def dfs(n):
    print(n, end=' ')
    visited[n] = True  # visited [False, False, False, False, False]
    for i in graph[n]:
        if not visited[i]:
            dfs(i)


# 너비 우선 탐색
def bfs(n):
    visited[n] = True
    queue = deque([n])
    while queue:    # 큐가 비어있지 않다면 반복 실행
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


dfs(v)
visited = [False] * (n + 1)
print()
bfs(v)

# graph
# [[] [] [] [] []]
# visited [False, False, False, False, False]
# queue
