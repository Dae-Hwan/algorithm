def solution(phone_book):
    dict = {}
    for p in phone_book:
        dict[p] = 1
    print(dict)

    for p in phone_book:
        if p in dict:
            return False
        temp = ""
        for letter in p:
            temp += letter
            if temp in dict and temp != p:  # p = 119
                return False

    return True