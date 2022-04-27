def solution(numbers, target):
    answer = 0

    def dfs(i, total):
        if i == len(numbers) and total == target:
            nonlocal answer
            answer += 1
            return
        if i == len(numbers):
            return

        dfs(i + 1, total + numbers[i])
        dfs(i + 1, total - numbers[i])

    dfs(0, 0)


    return answer

print(solution([1,1,1,1,1], 3))