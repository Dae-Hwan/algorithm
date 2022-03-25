def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0] - 1
        j = command[1]
        k = command[2] - 1

        sorted_array = sorted(array[i:j])
        answer.append(sorted_array[k])

    return answer