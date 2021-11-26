import sys

n = int(sys.stdin.readline())
n_stack_list = [0]

for i in range(2, n + 1):
    comparison = []

    if i % 3 == 0:
        three = i // 3  # 3으로 나눈 숫자
        # n_stack_list 가 인덱스 0부터 시작하기 때문에 맞춰서 값을 인덱스에 맞춰조정
        comparison.append(n_stack_list[three - 1])

    if i % 2 == 0:
        two = i // 2
        comparison.append(n_stack_list[two - 1])

    minus = i - 1
    comparison.append(n_stack_list[minus - 1])

    n_stack_list.append(min(i for i in comparison) + 1) # 맨마지막에 지금 한 행동을 추가해줘야하기 때문
    print(n_stack_list)

print(n_stack_list[-1])  # 가장 최신의 값을 빼줌