import sys

n = int(sys.stdin.readline())


for _ in range(n):
    zero = [1, 0]
    one = [0, 1]
    number = int(sys.stdin.readline())

    if number >= 2:
        for i in range(2, number + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])

    print(zero[number], one[number])





