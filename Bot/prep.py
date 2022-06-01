import os
import sys
import glob
import shutil


from database import *

if __name__ == '__main__':
    app_path = os.path.dirname(os.path.realpath(sys.argv[0]))  # Папка, откуда запускаемся
    data_path = os.path.join(app_path, 'data/'[:-1])
    os.makedirs(data_path, exist_ok=True)
    open('vk_bot_data.db', 'w').close()
    open('log.txt', 'w').close()
    db = Database()
    db.create_table('groups', [['user_id', 'INTEGER'], ['group_slug', 'VARCHAR(30)']])
    del db