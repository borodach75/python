# Подсчёт кол-ва часов по каждому из данных предметов

subj = {}
with open('text_6.txt', 'r', encoding='utf-8') as f:
    for l in f:
        l = l.split()
        subj[l[0]] = (sum([int(h.split('(')[0]) for h in l[1:] if h.split('(')[0].isdigit()]))
print(subj)