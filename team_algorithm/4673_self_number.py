def d(n):
    str_n = str(n)
    number_list = [str_n]

    sum = 0
    for index in range(len(str_n)):
        number_list.append(str_n[index])

    for each_number in number_list:
        sum += int(each_number)
    return sum


def self_number(number):
    all_number_list = []
    for n in range(1, number + 1):
        all_number_list.append(n)

    not_self_number_set = set()
    for n in range(1, number + 1):
        not_self_number_set.add(d(n))

    for n in not_self_number_set:
        if n < number + 1:
            all_number_list.remove(n)

    for i in all_number_list:
        print(i)


self_number(10000)
