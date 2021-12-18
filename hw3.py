"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
"""

n = input("Number is: ")
nn = n+n
nnn = n+n+n
print(f"{n} {nn} {nnn}")
print("Result is:",int(n)+int(nn)+int(nnn))
