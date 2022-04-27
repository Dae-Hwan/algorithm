def solution(n, computers):
    count = 0
    visited = [False for _ in range(n)]

    def dfs(com_idx, visited):
        visited[com_idx] = True
        for connect_idx in range(n):
            if connect_idx != com_idx and computers[com_idx][connect_idx] == 1:  # 다른 컴퓨터의 자기 컴퓨터 네트워크 선이 연결되어있고
                if visited[connect_idx] is False:  # 그 다른 컴퓨터를 확인했다면
                    dfs(com_idx, visited) # 그 컴퓨터로 이동한다.

    for com_idx in range(n):
        if not visited[com_idx]: # 방문 안한거라면
            dfs(com_idx, visited)
            count += 1

    return count

print(solution(3, [[1,1,0], [1,1,0], [0,0,1]]))