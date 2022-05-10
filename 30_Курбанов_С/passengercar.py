from car import Car
import pickle
from tee import *
import datetime


class PassengerCar(Car):

    def __init__(self, mark, power, production_year, number_of_passengers, repair_book):
        self.number_of_passengers = number_of_passengers
        self.repair_book = repair_book
        super().__init__(mark, power, production_year)
        sys.stdout.write(f'Создание экземпляра класса --- {datetime.datetime.now()} --- создано {self}\n')

    def __add__(self, repairs):
        self.repair_book.update(repairs)

    def __getitem__(self, date_of_repair):
        return f"Date of repair: {self.repair_book.get(date_of_repair)}"

    def clear_repair_book(self):
        print(f"Repair book is clear: {self.repair_book.clear()}")

    def __str__(self):
        return f"""
        Mark: {self.mark},
        Power: {self.power},
        Production year: {self.production_year},
        Number of passengers: {self.number_of_passengers},
        Repair book: {self.repair_book}"""


mers = PassengerCar('Mercedes', 230, 2002, 23, {'brakes': 2021})
bmw = PassengerCar('BMW', 2002, 330, 25, {'reels': 2014})
print(mers)
print(bmw)

p1 = open('pickk', 'wb')
pickle.dump(bmw, p1)
pickle.dump(mers, p1)
p1.close()
# del bmw
# del mers
