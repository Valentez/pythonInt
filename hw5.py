"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def sumCalc(inputString):
    inputList = inputString.split()
    sum = 0
    for i in inputList:
        if i:
            try:
                if i == "q":
                    return sum, False
                else:
                    sum += float(i)
            except ValueError:
                continue
    return sum, True


continueFlag = True
finalSum = 0
while continueFlag:
    inputString = input("Please, input two numbers via space. For exit enter q key: ")
    currentSum, continueFlag = sumCalc(inputString)
    finalSum += currentSum
    print("Intermediate sum: ", finalSum)
print("Result sum:", finalSum)
