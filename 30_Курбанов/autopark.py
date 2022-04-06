from passengercar import PassengerCar
from truck import Truck
from passengercar import mers, bmw
from truck import volvo, daf


class AutoPark:

    def __init__(self, name_of_autopark):
        super().__init__()
        self.name_of_autopark = name_of_autopark
        self.__passengerscar = []
        self.__trucks = []
        self.list_of_car = []

    def __str__(self):
        return f"""
        Name of autopark: {self.name_of_autopark},
        List of cars: {[i for i in self.passengers()]}, 
        List of trucks: {self.trucks_()}"""

    def passengers(self):
        try:
            for obj in self.__passengerscar:
                return obj
        except SyntaxError and ValueError as arr:
            print(f"Error check again: {arr}")

    def trucks_(self):
        try:
            for obj in self.__trucks:
                return obj
        except SyntaxError and ValueError as arr:
            print(f"Error check again: {arr}")

    def add_passenger(self, passenger, trucks):
        #if isinstance(passenger, PassengerCar):
            self.__passengerscar.append(passenger)
        #if isinstance(trucks, Truck):
            self.__trucks.append(trucks)

    def add_list(self):
        self.list_of_car.append(self.__trucks)
        self.list_of_car.append(self.__passengerscar)

    def __len__(self):
        return len(self.__trucks)

    def __getitem__(self, get_el):
        return self.list_of_car[get_el]

    # def __getitem__(self, get_el):
    #     return self.__passengerscar[get_el]

    def __sub__(self, del_el):
        del self.__trucks[del_el]

    def del_car(self, del_el):
        del self.__passengerscar[del_el]


if __name__ == '__main__':

    u = AutoPark('Fiyetville')
    u.add_passenger([mers, bmw], [volvo, daf])
    # u.add_passenger(bmw, daf)
    u.add_list()
    print(u['Volvo'])

