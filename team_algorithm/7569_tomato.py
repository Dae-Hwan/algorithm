import sys
from collections import deque

# M = 가로 N = 세로 H = 높이
M, N, H = map(int, sys.stdin.readline().split())
graph = []

for h in range(H):
    graph.append([])

    for n in range(N):
        graph[h].append(list(map(int, sys.stdin.readline().split())))

print(graph)


def bfs(graph, h, n, m):
    # 상하좌우
    plus_h = [0, 0, 0, 0, -1, 1]
    plus_n = [-1, 1, 0, 0, 0, 0]
    plus_m = [0, 0, -1, 1, 0, 0]

    queue = deque()
    queue.append((h, n, m))

    while queue:
        # 큐에서 뽑아낸 숫자 a, b
        queue_h, queue_n, queue_m = queue.popleft()

        # 토마토 큐에 추가하기
        for i in range(6):
            moved_h = queue_h + plus_h[i]
            moved_n = queue_n + plus_n[i]
            moved_m = queue_m + plus_m[i]

            # 토마토가 안들어있는 칸이면 넘어가
            if graph[queue_h][moved_n][moved_m] == -1:
                continue

            # 토마토가 안익었다면 익혀주기
            elif graph[moved_h][moved_n][moved_m] == 0:
                graph[moved_h][moved_n][moved_m] = graph[queue_h][queue_n][queue_m] + 1
                queue.append((moved_h, moved_n, moved_m))
                print(graph)


bfs(graph, 0, 0, 0)

present_max = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            present_max = max(present_max, graph[h][n][m])

print(present_max)