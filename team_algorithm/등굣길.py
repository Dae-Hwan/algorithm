from collections import deque

def bfs(graph, m, n):
    plus_sero = [1, 0]
    plus_garo = [0, 1]

    queue = deque()
    queue.append((0, 0))

    while queue:
        queue_sero, queue_garo = queue.popleft()

        for i in range(2):
            sero = queue_sero + plus_sero[i]
            garo = queue_garo + plus_garo[i]
            # print(sero, garo)

            if 0 <= sero < n and 0 <= garo < m and graph[sero][garo] is not False:
                # print('fefefefefe')
                if sero == 0:
                    graph[sero][garo] = graph[sero][garo - 1]
                    queue.append((sero, garo))

                elif garo == 0:
                    graph[sero][garo] = graph[sero - 1][garo]
                    queue.append((sero, garo))

                else:
                    # print('dulda')
                    graph[sero][garo] = graph[sero - 1][garo] + graph[sero][garo - 1]
                    queue.append((sero, garo))


def solution(m, n, puddles):  # m = 가로, n = 세로, puddles = 물웅덩이
    graph = [[0] * m for _ in range(n)]
    graph[0][0] = 1

    for p in puddles:
        print(p[0], p[1])
        garo = p[0] - 1
        sero = p[1] - 1
        graph[sero][garo] = False

    print(graph)

    bfs(graph, m, n)
    return graph[n - 1][m - 1]

print(solution(4, 3, [[2,2]]))

# 1, 1, 1, 1
# 1, 2, 3, 4
# 1, 3, 6, 10