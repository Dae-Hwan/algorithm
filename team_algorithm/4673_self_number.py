

def d(n):
    str_n = str(n)
    number_list = [str_n] #'3451' '3' '4' '5' '1' =

    for index in range(len(str_n)):
        number_list.append(str_n[index])

    sum = 0
    for each_number in number_list:
        sum += int(each_number)
    return sum
# print(d(3451))

def d2(n):
    result = n   # 3451 + 1 + 5 + 4 + 3
    while n > 0:
        result += n % 10
        n = n // 10  # 0
    return result
# print(d(3451))
#
not_self_num = set()
for num in range(1, 10001):
    result = d(num)
    if result < 10001:
        not_self_num.add(result)

for num in range(1, 10001):
    if num not in not_self_num:
        print(num)