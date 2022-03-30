from itertools import permutations


def solution(numbers):
    answer = 0
    ansSet = set()
    numList = []

    for i in range(len(numbers)):
        numList.append(numbers[i])

    permList = []

    for i in range(len(numbers)):
        permList += list(map("".join, permutations(numList, i + 1)))

    newList = [int(p) for p in permList]

    for item in newList:
        if item < 2: continue;

        check = True
        for i in range(2, int(item ** 0.5) + 1, 1):  # range 제곱근+1쓰는거 중요함
            if item % i == 0:
                check = False
                break
            if check == True:
                ansSet.add(item)

    answer = len(ansSet)
    return answer