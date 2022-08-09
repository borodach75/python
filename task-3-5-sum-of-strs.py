# Суммирование вводимых чисел

print('Для суммирования введите числа, разделённые пробелом. Для выхода введите иное.')
total = 0
exit_flag = False
while not exit_flag:
    local_sum = 0
    new_string = input().split()
    for num in new_string:
        if not num.isdigit():
            exit_flag = True
            break
        local_sum += int(num)
    total += local_sum
    print(f'{total} ({local_sum})')
