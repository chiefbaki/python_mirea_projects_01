import datetime


class Debug:
    def __init__(self, data: any = '', is_log: bool = True, key: str = 'LOG'):
            print(data)
            with open('data\log.txt', 'a') as f:
                f.write(f'{key} --- {str(datetime.datetime.now())} --- {data}\n')