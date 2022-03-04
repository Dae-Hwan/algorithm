import sys
from collections import deque


def bfs(h, w):
    # 상-하-좌-우-좌상-우상-좌하-우하
    plus_w = [0, 0, -1, 1, -1, 1, -1, 1]
    plus_h = [-1, 1, 0, 0, -1, -1, 1, 1]

    queue = deque()
    queue.append((h, w))

    while queue:
        queue_w, queue_h = queue.popleft()

        # 큐에 추가하기
        for i in range(8):
            moved_w = queue_w + plus_w[i]
            moved_h = queue_h + plus_h[i]

            # 범위안에 든다면
            if (0 <= moved_h < H) and (0 <= moved_w < W):
                # 이동한 곳이 바다면
                if graph[moved_h][moved_w] == 0:
                    continue

                # 이동한 곳이 섬이면
                elif graph[moved_h][moved_w] == 1:
                    graph[moved_h][moved_w] = 0
                    queue.append((moved_h, moved_w))


# w = 너비, h = 높이
W, H = map(int, sys.stdin.readline().split())
graph = [list(map(int, input().split())) for h in range(H)]

count = 0
for h in range(H):
    for w in range(W):
        if graph[h][w] == 1:
            count += 1
            bfs(h, w)
print(count)