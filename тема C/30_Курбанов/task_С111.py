"""
Каждый класс реализовать в отдельном модуле, импортируя их в производные модули.
Создать класс Car с полями марка, мощность, год производства. Добавить конструктор класса.
Создать производный от Car класс PassengerCar. Новые поля: количество пассажиров, ремонтная книжка
    (словарь вида запчасти: год замены). Определить конструктор, с вызовом родительского конструктора.
    Определить функции добавления замененной запчасти в ремонтную книжку, получения год замены по названию,
    форматированной печати всей ремонтной книжки. Переопределить метод преобразования в строку для печати
    основной информации (марка, мощность, год производства, количество пассажиров).
Создать производный от Car класс Truck. Новые поля: максимальная грузоподъемность, ФИ водителя, текущий груз
    (словарь вида название товара: вес). Определить конструктор, с вызовом родительского конструктора.
    Определить функции изменения водителя, добавления и удаления груза, форматированной печати текущего груза.
    Переопределить метод преобразования в строку для печати основной информации (марка, мощность, год производства,
    максимальная грузоподъемность, ФИ водителя).
Создать класс Autopark. Поля: название автопарка, список легковых машин (список экземпляров класса PassengerCar),
    список грузовиков (список экземпляров класса Truck). Определить конструктор. Переопределить метод
    преобразования в строку для печати всей информации об автопарке (с использованием переопределения в классах
    PassengerCar и Truck). Переопределить методы получения количества грузовиков функцией len, получения грузовой
    машины по индексу, изменения по индексу, удаления по индексу (пусть номера у грузовых машин считаются с 1,
    а индекс 0 – список всех легковых машин). Переопределить операции + и - для добавления или удаления грузовой
    машины. Добавить функцию создания txt-файла и записи всей информации в него (в том числе ремонтных
    книжек и списка грузов).
Предусмотреть хотя бы в 3 местах обработку возможных исключений.
В каждом модуле провести подробное тестирование всех создаваемых объектов и функций.
"""