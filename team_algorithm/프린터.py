def solution(priorities, location):
    order_priorities = [i for i in range(len(priorities))]
    sprint = 0

    while True:
        first_number = priorities.pop(0)
        first_index = order_priorities.pop(0)

        # 첫번째값이 가장 큰 값이면
        if first_number >= max(priorities):
            sprint += 1
            # 그 값이 location이면
            if location == first_index:
                return sprint

        else:
            priorities.append(first_number)
            order_priorities.append(first_index)