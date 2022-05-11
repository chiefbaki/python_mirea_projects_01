import os, shutil
import time
import re


def create_folder(source):
    try:
        if not os.path.isdir('Ознакомительная практика'):
            os.makedirs('Ознакомительная практика/Theme_A')  # создание папки
            os.makedirs('Ознакомительная практика/Theme_B')
            return "Файлы только что созданы"
    except FileExistsError as f:
        return "Файл уже создан"

    try:
        SOURCE_A_PATH = 'Ознакомительная практика/Theme_A'
        perm_A = os.stat(SOURCE_A_PATH).st_mode
        SOURCE_B_PATH = 'Ознакомительная практика/Theme_B'
        perm_B = os.stat(SOURCE_B_PATH).st_mode
        SOURCE_PATH = 'oper'
        files = os.listdir('oper')

        for file in files:
            if file[-7] == 'A':
                shutil.copyfile(source + '/' + file, SOURCE_A_PATH + '/' + file)
                print("File Permission mode:", perm_A)
            else:
                shutil.copyfile(source + '/' + file, SOURCE_B_PATH + '/' + file)
                print("File Permission mode:", perm_B)
    except shutil.SameFileError:
        print("Source and destination represents the same file.")
    except PermissionError:
        print("Permission denied.")


FOLDER_NAME = 'Ознакомительная практика'
path = os.getcwd() + f"\\{FOLDER_NAME}"


def run_files(path: str) -> None:
    pattern = r"def (\w+\(\w+\))"
    folders = [name for name in os.listdir(
        path) if os.path.isdir(os.path.join(path, name))]
    for folder in folders:
        print(f'folder "{folder}"')
        for file in os.listdir(os.path.join(path, folder)):
            if file.endswith('.py'):
                print(f'script "{file}"')
                start = time.time()
                source = open(os.path.join(path, folder, file)).read()
                functions = re.findall(pattern, source)
                print(f'function - "{functions}"')
                print('output - ')
                exec(open(os.path.join(path, folder, file)).read(), globals())
                stop = time.time()
                print('time "%s"s' % (stop - start))




    # SOURCE_PATH = 'oper'
    # perm = os.stat(SOURCE_PATH).st_mode
    # files = create_folder(SOURCE_PATH)
    # print(files)
    # print("File Permission mode:", perm, "\n")

print(run_files(path))

