import sys


def memo(number):
    if number >= len(dp):
        for i in range(len(dp), number + 1):
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

    print(dp[number])


T = int(sys.stdin.readline())
dp = [0, 1, 2, 4]

for _ in range(T):
    number = int(sys.stdin.readline())
    memo(number)

# # 1
# 1

# #2
# 1, 1 + 2
# 2 + 2

# # 3
# 1, 1, 1
# 2, 1
# 1, 2
# 3

# # 4
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1