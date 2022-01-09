"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
GoogleTranslate = {"One": "Odin",
                   "Two": "Dva",
                   "Three": "Tri",
                   "Four": "Chetyre",
                   "Five": "Pyat",
                   "Six": "Shest",
                   "Seven": "Sem"}
with open("hw54Source.txt") as fileRead, open("hw54Result.txt", "w") as fileWrite:
    for line in fileRead.readlines():
        txtNum, num = line.rstrip().split(' - ')
        fileWrite.write(f"{GoogleTranslate[txtNum]} - {num}\n")
