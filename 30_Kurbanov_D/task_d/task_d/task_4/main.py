import os
import sys
import jsd
import time


BASE_FOLDER_NAME = "Ознакомительная папка"

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
                print(f'function - "{functions[0]}"')
                print('output - ')
                exec(open(os.path.join(path, folder, file)).read(), globals())
                stop = time.time()
                print('time "%s"s' % (stop - start))


if __name__ == "__main__":
    # base_dir = move_files()
    base_dir = os.getcwd() + f"\\{BASE_FOLDER_NAME}"
    run_files(base_dir)
