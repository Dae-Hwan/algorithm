import sys

n = int(sys.stdin.readline())

bong_ji = [-1, -1, -1, 1, -1, 1]  # 인덱스 5까지 넣음
for i in range(6, n + 1):
    print(i)
    comparison = []  # 비교를 위한 리스트
    if bong_ji[i - 3] != -1:
        print("three")
        minus_by_three = i - 3
        previous_index_minus_by_three = bong_ji[minus_by_three]
        comparison.append(previous_index_minus_by_three)

    if bong_ji[i - 5] != -1:
        print("five")
        minus_by_five = i - 5
        previous_index_minus_by_five = bong_ji[minus_by_three]
        comparison.append(previous_index_minus_by_five)

    if len(comparison) == 0:
        print("minus")
        bong_ji.append(-1)
        print(comparison)

    else:
        print(comparison)
        bong_ji.append(min(i for i in comparison) + 1)

    print(bong_ji)

# 5로 뺄 수 있을때까지 뺀다음 3을 뺀다. -> 그리디 알고리즘
18 -> 5 - 5 - 5 -3
# 정당성 검사 ->

# 18 -> 3 * 6
# 18 -> 5 * 1 + 3 * 1
# 3의 배수면 3을 빼
# 5의 배수면 집어넣음
# 3를 빼보자
# 5를 빼보자
# 3 또는 5로 나뉠 수 있으면 3을 빼보고 5를빼봄
# 없다면 -1 집어넣음

### 문제 이해
### 대략적인 코드설명
### 접근 방법
# 사용시기
# 정당성 검사
### 시간복잡도 계산
