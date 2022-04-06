def solution(name):
    sprint = -1

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    for n in name:
        print(n, alphabet.index(n))
        if alphabet.index(n) <= len(alphabet) // 2:
            i = 0
            while i < len(alphabet):
                if n == alphabet[i]:
                    print(i, alphabet[i], sprint)
                    break
                sprint += 1
                i += 1

        elif alphabet.index(n) > len(alphabet) // 2:
            i = len(alphabet) - 1
            while i > 0:
                if n == alphabet[i]:
                    print(i, alphabet[i], sprint)
                    break
                sprint += 1
                i -= 1
        sprint += 1

        # print(sprint)
    return sprint

print(solution("JEROEN"))
print(solution("JAZ"))
print(solution("JAN"))