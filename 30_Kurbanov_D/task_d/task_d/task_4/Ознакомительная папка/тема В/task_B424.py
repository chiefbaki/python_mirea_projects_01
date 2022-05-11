"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""


def filtre_function(str):
    white_list = set('abcdefghijklmnopqrstuvwxy ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in str:
        if not(i in white_list):
            return False
    return True


def wiki_function():
    file = open("input.txt")
    lines = file.readlines()  # Создаем список со считанными строками
    while "\n" in set(lines):  # Удаляем пустые строки из списка
        lines.remove("\n")
    print("Текст из файла:\n")
    for i in lines:
        print(i)
    file.close()

    # Удаляем все символы, кроме пробелов и латинских букв
    for i in range(len(lines)):
        lines[i] = ''.join(filter(filtre_function, lines[i]))
    print("\n\nУдаление всех символов, кроме латинских бкув и пробелов:\n")
    for i in lines:
        print(i, "\n")

    # Объединяем все строки в одну
    text = " ".join(lines)

    # Cоздание словаря
    my_dict = dict()
    txt_arr = text.split()
    for i in txt_arr:
        my_dict[i] = my_dict.get(i, 0) + 1
    print("Словарь: ")
    print(my_dict, "\n")

    # Вывод 10 самых популярных слов
    words = [""] * 10
    # Создаем отсортированный по возрастанию список кортежей
    list_sorted = sorted(my_dict.items(), key=lambda x: (x[1]))
    list_sorted.reverse()  # Переворачиваем список
    k = 0
    print("10 самых часто встречающихся слов в предложении:")
    for key, value in list_sorted:
        words[k] = key
        k += 1
        print(k, "place ---", key, "---", value, "times")
        if (k == 10):
            break

    # Заменяем 10 самых популярных слов на подстроку "PYTHON"
    for w in words:
        for i in range(len(txt_arr)):
            if (txt_arr[i] == w):
                txt_arr[i] = "PYTHON"
    text = " ".join(txt_arr)
    print("\n\nЗамена слов в предложении: ")
    print(text, "\n")

    # Записываем новую строку в файл, разбивая ее на строки не более 100 символов
    new_wiki_lines = []
    new_file = open("output.txt", "w")
    l = txt_arr[0]
    for i in range(1, len(txt_arr)):
        if len(l + " " + txt_arr[i]) < 100:
            l += " " + txt_arr[i]
        else:
            new_wiki_lines.append(l)
            l = txt_arr[i]
    new_wiki_lines.append(l)
    print("В файл будет записан следующий текст:")
    for w in new_wiki_lines:
        print(w)
        new_file.write(w + '\n')
    new_file.close()


wiki_function()
