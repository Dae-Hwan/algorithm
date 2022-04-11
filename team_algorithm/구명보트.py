def solution(people, limit):
    answer = 0
    people.sort()  # 오름차순 정렬

    left = 0  # 가장 작은 수
    right = len(people) - 1  # 가장 큰수

    while left <= right:  # 작은수의 인덱스가 큰수의 인덱스를 따라잡을 때까지
        if people[left] + people[right] <= limit:  # 보트무게봐 작으면
            left += 1  # 작은수 + 1
            right -= 1  # 큰수 - 1
        else:  # 보트무게보다 몸무게가 크면
            right -= 1  # 한사람만 태울 수있으므로

        answer += 1  # 보트 하나끝
    return answer