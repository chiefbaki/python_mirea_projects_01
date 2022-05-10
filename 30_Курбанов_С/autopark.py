from truck import *
from passengercar import *
from tee import *


class AutoPark:

    def __init__(self, name_of_autopark):
        self.name_of_autopark = name_of_autopark
        self._passengerscar = []
        self._trucks = []
        self.__list_of_cars = []

    def __str__(self):
        return f"""
        Name of autopark: {self.name_of_autopark},
        List of cars: {self.passengers()}, 
        List of trucks: {self.trucks_()}
        """

    def passengers(self):
        try:
            s = ''
            for obj in self._passengerscar:
                s += str(obj)
            return s
        except SyntaxError and ValueError as arr:
            sys.stdout.write(f'ERR --- {datetime.datetime.now()} --- распечатаны {self}\n')
            print(f"Error check again: {arr}")

    def trucks_(self):
        try:
            b = ''
            for obj in self._trucks:
                b += str(obj)
            return b
        except SyntaxError and ValueError as arr:
            print(f"Error check again: {arr}")
            sys.stdout.write(f'ERR --- {datetime.datetime.now()} --- распечатаны {self}\n')

    def add_car(self, p1):
        self._passengerscar.append(p1)

    def add_truck(self, trucks):
        self._trucks.append(trucks)

    def __len__(self):
        return len(self._trucks)

    def getter(self):
        for i in self._trucks:
            print(i)

    def __getitem__(self, get_el):
        return self._trucks[get_el]

    def __delitem__(self, del_item):
        return self._trucks.pop(del_item)

    def __setitem__(self, key, value):
        self._trucks[key] = value

    def __sub__(self, del_el):
        del self._trucks[del_el]

    def del_car(self, del_el):
        del self._passengerscar[del_el]


u = AutoPark('Fiyetville')
u.add_car(bmw)
u.add_car(mers)
u.add_truck(volvo)
u.add_truck(daf)
u.add_truck(ford)

print(u)
