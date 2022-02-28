import sys

n = int(sys.stdin.readline().strip())
jump_1 = []  # 한칸 점프
jump_2 = []  # 두칸 점프

for i in range(1, n + 1):
    score = int(sys.stdin.readline().strip())

    if i == 1:
        jump_1.append(score)
        jump_2.append(0)

    elif i == 2:
        jump_1.append(jump_1[-1] + score)
        jump_2.append(score)

    else:
        jump_1.append(jump_2[-1] + score)
        jump_2.append(max(jump_1[-3], jump_2[-2]) + score)

print(max(jump_1[-1], jump_2[-1]))


# 점수     10  20  15  25  10  20
# 계단  0  1   2   3   4   5   6
# 한칸  0  10  30  35  50  65  65
# 두칸  0  0   20  25  55  45  75