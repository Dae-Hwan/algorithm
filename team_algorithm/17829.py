import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def square(n, paper):
    if n == 1:
        return
    else:
        for x in range(0, N, 2):
            for y in range(0, N, 2):
                print(x, y)

square(N, paper)