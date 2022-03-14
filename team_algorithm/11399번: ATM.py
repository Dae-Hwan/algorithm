import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

sum = 0
sum_list = []
for number in numbers:
    sum += number
    sum_list.append(sum)


result = 0
for i in sum_list:
    result += i

print(result)
