import sys
from collections import deque


def bfs(graph, a, b):
    # 상하좌우(헷갈리지 말아야할게 x가 x축 이 아니라 y축임)
    plus_a = [-1, 1, 0, 0]
    plus_b = [0, 0, -1, 1]

    queue = deque()
    queue.append((a, b))

    while queue:
        # 큐에서 뽑아낸 숫자 a, b
        a, b = queue.popleft()

        # 상하좌우 넣어봐서 있으면 큐에 추가하기
        for i in range(4):
            moved_a = a + plus_a[i]
            moved_b = b + plus_b[i]

            if graph[moved_a][moved_b] == 0:
                continue

            if graph[moved_a][moved_b] == 1:
                graph[moved_a][moved_b] = 0
                queue.append((moved_a, moved_b))


T = int(sys.stdin.readline())

for _ in range(T):
    count = 0
    # M = 가로 N = 세로 K = 배추 수
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * (M + 2) for _ in range(N + 2)]

    # 배추 심기
    for _ in range(K):
        b, a = map(int, sys.stdin.readline().split())
        graph[a + 1][b + 1] = 1

    # 차례대로 보는데, 배추가 위치에 있으면 bfs 돌리기
    for a in range(N):
        for b in range(M):
            if graph[a + 1][b + 1] == 1:
                bfs(graph, a + 1, b + 1)
                count += 1

    print(count)