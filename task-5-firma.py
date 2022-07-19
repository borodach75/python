# Расчёт прибыли и рентабельности фирмы

vyruchka = int(input('Введите значение выручки фирмы: '))
izderzhki = int(input('Введите значение издержек: '))
pribyl = vyruchka - izderzhki
if pribyl == 0:
    print('Фирма вышла в 0')
elif pribyl < 0:
    print('Фирма отработала в убыток со значением', pribyl)
else:   # pribyl > 0
    print('Фирма отработала с прибылью:', pribyl)
    print(f'Рентабельность составила: {pribyl / vyruchka :.3f}')
    chislennost = int(input('Введите численность сотрудников фирмы: '))
    print(f'Прибыль фирмы в расчёте на одного сотрудника составила: {pribyl / chislennost :.2f}')
