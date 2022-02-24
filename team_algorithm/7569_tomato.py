import sys
from collections import deque

# M = 가로 N = 세로 H = 높이
M, N, H = map(int, sys.stdin.readline().split())
graph = []
count = 0

for h in range(H):
    graph.append([])

    for n in range(N):
        graph[h].append(list(map(int, sys.stdin.readline().split())))

print(graph)


def bfs(graph, h, n, m):
    count = 0

    # 상하좌우
    plus_h = [0, 0, 0, 0, -1, 1]
    plus_n = [-1, 1, 0, 0, 0, 0]
    plus_m = [0, 0, -1, 1, 0, 0]

    queue = deque()
    queue.append((h, n, m))

    while queue:
        count += 1
        # 큐에서 뽑아낸 숫자 a, b
        queue_h, queue_n, queue_m = queue.popleft()

        # 토마토 큐에 추가하기
        for i in range(6):
            moved_h = queue_h + plus_h[i]
            moved_n = queue_n + plus_n[i]
            moved_m = queue_m + plus_m[i]

            # moved_h가 0 이거나 범위안에들고
            if 0 <= moved_h < h and 0 <= moved_n < n and 0 < moved_m < m:
                # 토마토가 안익었다면 익혀주기
                if graph[moved_h][moved_n][moved_m] == 0:
                    graph[moved_h][moved_n][moved_m] = 1
                    queue.append((queue_h, moved_n, moved_m))

            if graph[queue_h][moved_n][moved_m] == 1:
                continue


bfs(graph, h, n, m)

