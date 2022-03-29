def solution(answers):
    # answer는 정답이 순서대로
    pattern_one = [1, 2, 3, 4, 5]
    pattern_two = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = {1: 0, 2: 0, 3: 0}

    for i, a in enumerate(answers):
        if a == pattern_one[i % len(pattern_one)]:
            score[1] += 1

        if a == pattern_two[i % len(pattern_two)]:
            score[2] += 1

        if a == pattern_three[i % len(pattern_three)]:
            score[3] += 1

    answer = []

    max_value = max(score.values())
    for key, value in score.items():
        if max_value == value:
            answer.append(key)
        else:
            continue

    return sorted(answer)