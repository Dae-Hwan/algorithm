from collections import deque
import sys

# 뽑아내는데는 sprint 0 이동하면 sprint
n, m = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))
numbers = deque([i for i in range(1, n + 1)])

sprint = 0
for i in range(m):
    target = targets[i]
    index = numbers.index(target)

    if (len(numbers) / 2) >= index:
        while True:
            if target == numbers[0]:
                numbers.popleft()
                break

            else:
                numbers.rotate(-1)
                sprint += 1
    else:
        while True:
            if target == numbers[0]:
                numbers.popleft()
                break
            else:
                numbers.rotate(1)
                sprint += 1

print(sprint)

