import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    if N % H == 0:
        floor = H
        ho = N // H
    else:
        floor = N % H
        ho = N // H + 1

    print(floor * 100 + ho)