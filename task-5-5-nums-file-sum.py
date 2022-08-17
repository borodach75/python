# Числа записываем в файл, считываем их из него, суммируем

nums = [1 / x for x in range(1, 21)]
with open('text5-5.txt', 'w', encoding='utf-8') as my_f:
    print(*nums, file=my_f)
with open('text5-5.txt', 'r', encoding='utf-8') as my_f:
    nums_inp = list(map(float, my_f.read().split()))
    print(sum(nums_inp))