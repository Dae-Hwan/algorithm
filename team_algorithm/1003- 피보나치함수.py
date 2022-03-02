# import sys
#
# T = int(sys.stdin.readline())
#
# for _ in range(T):
#     number = int(sys.stdin.readline())
#     zero = [1, 0]
#     one = [0, 1]
#
#     if number > 3:
#         for i in range(2, number + 1):
#             zero.append(zero[i - 1] + zero[i - 2])
#             one.append(one[i - 1] + one[i - 2])
#
#     print(zero[number], one[number])

# 런 타임 에러 -> 계속 새로운 리스트를 만들어서 그런거 같음

# import sys
#
#
# def fibonacci(number):
#
#     if number >= len(zero):
#         for i in range(len(zero), number + 1):
#             zero.append(zero[i - 1] + zero[i - 2])
#             one.append(one[i - 1] + one[i - 2])
#
#     print(zero[number], one[number])
#
#
# T = int(sys.stdin.readline())
# zero = [1, 0]
# one = [0, 1]
#
# for _ in range(T):
#     number = int(sys.stdin.readline())
#     fibonacci(number)
#
#
# ------------
import sys

input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

dp = [[0, 0] for _ in range(41)]

dp[0] = [1, 0]
dp[1] = [0, 1]
dp[2] = [1, 1]
dp[3] = [1, 2]
dp[4] = [2, 3]

for i in range(5, 41):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

for i in nums:
    print(dp[i][0], end=' ')
    print(dp[i][1])