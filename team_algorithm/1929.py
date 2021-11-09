def check(num):
    if num == 1:
        return False
    else:
        # 2부터 num까지의 제곱근까지만 검사하면 됨
        # 안그러면 시간초과가 뜸
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if check(i):
        print(i)