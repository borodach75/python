# Расчёт прибыли компаний и их средней прибыли, запись в JSON

import json

firms = {}
count = summ = 0
with open('text_7.txt', 'r', encoding='utf-8') as my_f:
    for line in my_f:
        line = line.split()
        firms[line[0]] = profit = int(line[2]) - int(line[3])
        if profit > 0:
            count += 1
            summ += profit
with open('text_71.json', 'w', encoding='utf-8') as my_j:
    json.dump([firms, {'average_profit': summ / count}], my_j)
