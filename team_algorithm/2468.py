import sys
import math
from collections import deque

def bfs(a, b):
    # 상-하-좌-우
    plus_a = [-1, 1, 0, 0]
    plus_b = [0, 0, -1, 1]
    queue = deque()
    queue.append((a, b))


    while queue:
        queue_a, queue_b = queue.popleft()
        graph[queue_a][queue_b] = 0

        for i in range(4):
            moved_a = queue_a + plus_a[i]
            moved_b = queue_b + plus_b[i]

            # 범위안에 든다면
            if (0 <= moved_a < N) and (0 <= moved_b < N):
                # 이동한 곳이 N보다 크면
                if graph[moved_a][moved_b] > N:
                    graph[moved_a][moved_b] = 0
                    queue.append((moved_a, moved_b))
                    continue

                # 이동한 곳이 N 이하이면
                elif graph[moved_a][moved_b] <= N:
                    continue


N = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for n in range(N)]

count = 0
for a in range(N):
    for b in range(N):
        if graph[a][b] > N:
            print(a, b)
            count += 1
            bfs(a, b)
            print(graph)
print(count)
