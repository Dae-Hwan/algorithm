import sys

n = int(sys.stdin.readline())
color = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    color[i][0] += min(color[i - 1][1], color[i - 1][2])
    color[i][1] += min(color[i - 1][0], color[i - 1][2])
    color[i][2] += min(color[i - 1][0], color[i - 1][1])
print(min(color[-1]))



# 최솟값만 고르는 방식으로 가다간 밑에 처럼 반례가 나온다
# 1   100   100
# 100 100 101
# 100 1   50
#
# 151
# 103

# 값을 후보 두개를 넣어놓고 지금꺼 두개 가 정해지면 비교해서

#  | 0  1  2  3  4  5  6  7  8  9
# R| 10 2  4  2  6  5
# G| 9  5  3  1  5  5
# B| 7  8  7  2  4  5

#  | 0  1  2  3  4  5  6  7  8  9
# R| 10 9  16
# G| 9  12 12
# B| 7  17 16

