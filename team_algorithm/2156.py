import sys

n = int(sys.stdin.readline().strip())
jump_1 = []
jump_2 = []
jump_3 = []

if n == 0:
    print(0)

else:
    for i in range(1, n + 1):
        amount = int(sys.stdin.readline().strip())

        if i == 1:
            jump_1.append(amount)
            jump_2.append(0)
            jump_3.append(0)

        elif i == 2:
            jump_1.append(jump_1[-1] + amount)
            jump_2.append(amount)
            jump_3.append(0)

        elif i == 3:
            jump_1.append(jump_2[-1] + amount)
            jump_2.append(max(jump_1[-3], jump_2[-2]) + amount)
            jump_3.append(0)

        else:
            jump_1.append(max(jump_2[-1], jump_3[-1]) + amount)
            jump_2.append(max(jump_1[-3], jump_2[-2], jump_3[-2]) + amount)
            jump_3.append(max(jump_1[-4], jump_2[-4], jump_3[-3]) + amount)

    print(max(max(jump_1), max(jump_2), max(jump_3)))

# 점수   0  6  10  13  9   8   1
# 포도   0  1  2   3   4   5   6
# 한칸   0  6  16  23  28  33  32    max(두칸[-1], 세칸[-1]) * amount
# 두칸   0  0  10  19  25  31  29    max(한칸[-2], 두칸[-2]) + amount
# 세칸   0  0  0   13                max(한칸[-3] 두칸[-3]) + amount

#### 두번 연속으로 안마시는 경우
# 점수   0  1000  1000  1     1     1000  1000
# 포도   0  1     2     3     4     5     6
# 한칸   0  1000  2000  1003  1002  3001  3003
# 두칸   0  0     1000  1001  2001  2003
# 세칸   0  0     0     1     1001  3000  4000

# 방법론이 아예 틀렸나?..


# 연속으로 안마시는게 일상화되면 답이없는데..
# 연속으로 마시는거랑
# 한칸 쉬고 마시는거랑
# 두칸 쉬고 마시는 거랑
# 이렇게 3개를 비교해야되나?
