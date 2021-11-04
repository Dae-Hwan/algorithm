import sys


def sort_coordinates():
    n = int(sys.stdin.readline())

    array = []

    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        array.append([y, x])

    array.sort()

    for i in range(n):
        print(array[i][1], array[i][0])


sort_coordinates()


def sort_coordinates():
    n = int(sys.stdin.readline())

    array = []

    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        array.append([x, y])
    print(array)
    array.sort(key=lambda c: (c[1], c[0]))
    print(array)

    for i in range(n):
        print(array[i][0], array[i][1])


sort_coordinates()