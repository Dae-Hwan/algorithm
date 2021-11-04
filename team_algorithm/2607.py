# 최대공약수 -> 1부터 작은수 까지의 수중 가장 큰 공약수
# 공약수 -> 두수가 모두 1이 아닌 자연수로 나눠지는 수 -> 두값다 나머지가 0 이되는 1이 아닌 수
# 최소공배수 -> 최대공약수 * (큰수//최대공약수) * (작은수//최대공약수)

import sys
num = list(map(int, sys.stdin.readline().split()))

small_num = min(num)
big_num = max(num)

gcd = 0

for i in range(1, small_num + 1):
    if small_num % i == 0 and big_num % i == 0:
        gcd = i

small_num_measure = small_num // gcd
big_num_measure = big_num // gcd

print(gcd)
print(small_num_measure * big_num_measure * gcd)

