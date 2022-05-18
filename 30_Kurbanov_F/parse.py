# import requests
# from bs4 import BeautifulSoup


class ParseData:

    def __init__(self, url):
        self._page = requests.get(url)
        self._soup = BeautifulSoup(self._page.text, 'html.parser')
        self._result = None
        self._f1 = None
        self._f2 = None
        self._f3 = None

    def find(self):
        self._result = self._soup.find('div', {'class': 'rasspisanie'}).\
            find(string='Институт информационных технологий').\
            find_parent('div').\
            find_parent('div')

        for x in self._result.find_all('a', class_='uk-link-toggle'):
            link = x.get('href')
            self._f1 = open('1-kurs.xlsx', 'wb')
            self._f2 = open('2-kurs.xlsx', 'wb')
            self._f3 = open('3-kurs.xlsx', 'wb')

            resp1 = requests.get(
                'https://webservices.mirea.ru/upload/\
                iblock/10f/4hou1bgun6zg3ej93bzi859yct743gsf/\
                ИИТ_1 курс_21-22_весна_очка.xlsx')
            resp2 = requests.get(
                'https://webservices.mirea.ru/upload/\
                iblock/76d/0v88kk2b3mb0uvxc187fho0f4thmua68/\
                ИИТ_2 курс_21-22_весна_очка.xlsx')
            resp3 = requests.get(
                'https://webservices.mirea.ru/upload/\
                iblock/995/km8f4ocqffyf2j42c7mtaq4er2ibk3o7/\
                ИИТ_3 курс_21-22_весна_очка.xlsx')

            self._f1.write(resp1.content)
            self._f2.write(resp2.content)
            self._f3.write(resp3.content)


if __name__ == '__main__':
    data = ParseData('https://www.mirea.ru/schedule/')
    data.find()
    