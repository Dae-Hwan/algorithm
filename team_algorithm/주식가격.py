from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        now_price = queue.popleft()
        count = 0
        for future_price in queue:
            count += 1
            if now_price <= future_price:
                continue
            else:
                break
        answer.append(count)

    return answer