import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n + 1)

print(graph)


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            print(i)
            dfs(graph, i, visited)
    return True


dfs(graph, 1, visited)

print(sum(visited) - 1)  # 방문한 컴퓨터 개수 - 1번 컴퓨터
