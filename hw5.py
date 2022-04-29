"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым
результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность
выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

pribil = float(input("Vyruchka firmy: "))
traty = float(input("Traty firmy: "))

profit = pribil-traty

if profit > 0:
    print(f'Rentabelnost ravna {profit/pribil*100:.2f}%')
    workers = int(input("Vvedite kol-vo sotrudnikov: "))
    print(f"Pribyl na sotrudnika - {profit/workers}")
elif profit < 0:
    print("Firma rabotaet v minus")
else:
    print("U firmy nulevaya pribyl")
    
