from car import Car
import pickle
from tee import *
import datetime


class Truck(Car):

    def __init__(self, mark, power, production_year, maximum_capacity, name_surname, current_cargo):

        self.maximum_capacity = maximum_capacity
        self.name_surname = name_surname
        self.current_cargo = current_cargo
        super().__init__(mark, power, production_year)
        sys.stdout.write(f'CRE --- {datetime.datetime.now()} --- создано {self}\n')

    def change_driver(self, new_driver):
        self.name_surname = new_driver
        print(f"New driver is {new_driver}")
        sys.stdout.write(f'INF --- {datetime.datetime.now()} --- изменены {self}\n')

    def __sub__(self, del_cargo):
        try:
            self.current_cargo.pop(del_cargo)
        except TypeError:
            print("Be attention")

    def __add__(self, cargo):
        self.current_cargo.update(cargo)
        sys.stdout.write(f'CRE --- {datetime.datetime.now()} --- добавлен {self.current_cargo}\n')

    def format_cargo(self):
        print(f"Format cargo: {self.current_cargo.clear()}")
        sys.stdout.write(f'CRE --- {datetime.datetime.now()} --- удален {self}\n')

    def __str__(self):
        return f"""
            Mark: {self.mark},
            Power: {self.power},
            Production year: {self.production_year},
            Maximum capacity : {self.maximum_capacity},
            Name and Surname: {self.name_surname},
            Current cargo: {self.current_cargo}"""


volvo = Truck('Volvo', 450, 2015, 2500, 'John Dodson', {'TV': 500, 'fridge': 500})
ford = Truck('Ford', 450, 2015, 3000, 'Jorge John', {'DVD': 100, 'fridge': 500})
daf = Truck('DAF', 500, 2020, 2600, 'Jay Ray', {'jeans': 4500, 'T-shirts': 5000})

volvo.change_driver("Joseph Benavidez")
volvo + {'dresses': 22424}

p2 = open('pickk', 'wb')
pickle.dump(volvo, p2)
pickle.dump(ford, p2)
pickle.dump(daf, p2)
p2.close()
# del volvo
# del ford
# del daf
