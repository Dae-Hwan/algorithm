import sys
from collections import deque


def bfs(a, b):
    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    plus_a = [-1, 1, 0, 0]
    plus_b = [0, 0, -1, 1]
    queue = deque()
    queue.append((a, b))
    size = 1

    while queue:
        queue_a, queue_b = queue.popleft()
        graph[queue_a][queue_b] = 1

        for i in range(4):
            moved_a = queue_a + plus_a[i]
            moved_b = queue_b + plus_b[i]

            # 범위안에 든다면
            if (0 <= moved_a < M) and (0 <= moved_b < N):
                # 이동한 곳이 N보다 크면
                if graph[moved_a][moved_b] == 0:
                    graph[moved_a][moved_b] = 1
                    queue.append((moved_a, moved_b))
                    size += 1

    return size


# M = 높이 N = 길이 K = 횟수
M, N, K = map(int, sys.stdin.readline().split())
graph = [(N) * [0] for m in range(M)]

for k in range(K):
    a1, b1, a2, b2 = map(int, sys.stdin.readline().split())
    # print(a1, b1, a2, b2)

    for b in range(b2 - b1):
        for a in range(a2 - a1):
            # print(b1 + b, a1 + a)
            if 0 <= b1 + b < M and 0 <= a1 + a <= N:
                # print(b1 + b, a1 + a)
                if graph[b1 + b][a1 + a] == 0:
                    graph[b1 + b][a1 + a] = 1

count = 0
size = []
for m in range(M):
    for n in range(N):
        if graph[m][n] == 0:
            # print(graph)
            # print(m, n)
            count += 1
            size.append(bfs(m, n))
size.sort()
print(count)
for i in size:
    print(i, end=' ')

# 영역의 개수
# 영역의 넓이

# [0, 0, 0, 0, 1, 1, 0]
# [0, 1, 0, 0, 1, 1, 0]
# [2, 1, 1, 1, 0, 0, 0]
# [1, 1, 1, 2, 0, 0, 0]
# [0, 1, 0, 0, 0, 0, 0]

# (0,2)(4,4)

# (0, 0) (7, 5)

[[0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0],
 [0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 2, 0, 0, 2, 2, 0, 0, 2, 0, 2, 0, 0],
 [0, 2, 0, 0, 2, 2, 0, 0, 2, 2, 2, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0]])