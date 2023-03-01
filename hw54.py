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
translate_dict = {"One": "Odin",
                   "Two": "Dva",
                   "Three": "Tri",
                   "Four": "Chetyre",
                   "Five": "Pyat",
                   "Six": "Shest",
                   "Seven": "Sem"}
with open("hw54Source.txt") as file_read, open("hw54Result.txt", "w") as file_write:
    for line in file_read.readlines():
        txt_num, num = line.rstrip().split(' - ')
        file_write.write(f"{translate_dict[txt_num]} - {num}\n")
