while True:
    sentence = input()
    stack = []

    if sentence == ".":
        break

    for s in sentence:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            # 길이가 0이면 이미 no 이기 때문
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break

        elif s == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break

    if len(stack) == 0:
        print('yes')
    else:
        print('no')