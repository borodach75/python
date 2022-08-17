# Поиск сотрудников по окладу, подсчёт средней величины оклада

print('Сотрудники с зарплатой меньше 20 тысяч:')
with open('text_3.txt', 'r', encoding='utf-8') as my_f:
    count = summ = 0
    for line in my_f:
        name, sal = line.strip().split()
        sal = float(sal)
        count += 1
        summ += sal
        if sal < 20000:
            print(line, end='')
print('Величина среднего оклада:', summ / count)
