# import sys
#
#
# def solve():
#     n = int(sys.stdin.readline().rstrip())
#     arr = [0]
#     for _ in range(n):
#         x = int(sys.stdin.readline().rstrip())
#         arr.append(x)
#     g = [0, 0]
#     h = [0, arr[1]]
#     for i in range(2, n + 1):
#         g.append(h[i - 1] + arr[i])
#         h.append(max(h[i - 2], g[i - 2]) + arr[i])
#     print(max(g[n], h[n]))
#
#
# solve()

#     10  20  15  25  10  20
# 0   1   2   3   4   5   6
# 0   10  30  35  50  65  65   g(x)
# 0   0   20  25  55  45  75   h(x)

# f(x) = max(g(x), h(x))
# g(x) = h(x-1) + arr[x]  # 다음계단으로 갈수없는애(시작점에는 연속으로 3번가능)
# h(x) = max(g(x -2 ), h(x -2 )) + arr[x]  # 다음계단을 갈 수 있는애


n = int(input())
point = []

for i in range(n):
    point.append(int(input()))
print(point)

if input == 1:
    print(point[0])
else:
    s = [0] * 300
    s[1] = point[1]
    s[2] = point[1] + point[2]

    for i in range(5, 6):
        print(s[i - 3] + point[i - 1] + point[i])
        print(s[i - 2] + point[i])
        s[i] = max(s[i - 3] + point[i - 1] + point[i], s[i - 2] + point[i])
        print(s[i])
    print(s[n])
