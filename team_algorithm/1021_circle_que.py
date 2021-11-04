import sys

n, m = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))
numbers = [i for i in range(1, n + 1)]

sprint = 0
for i in range(m):
    target = targets[i]
    index = numbers.index(target)

    if len(numbers) / 2 >= target:
        while True:
            if target == numbers[0]:
                del numbers[0]
                break
            else:
                numbers.append(numbers[0])
                del numbers[0]
                sprint += 1
    else:
        while True:
            if target == numbers[0]:
                del numbers[0]
                break
            else:
                numbers.insert(0, numbers[-1])
                del numbers[-1]
                sprint += 1

print(sprint)