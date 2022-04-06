from car import Car


class Truck(Car):

    def __init__(self, mark, power, production_year, maximum_capacity, name_surname, current_cargo):
        super().__init__(mark, power, production_year)

        self.maximum_capacity = maximum_capacity
        self.name_surname = name_surname
        self.current_cargo = current_cargo

    # Смена водителя

    def change_driver(self, new_driver):
        self.name_surname = new_driver
        print(f"New driver is {new_driver}")

    # Удаление груза

    def __sub__(self, del_cargo):
        try:
            self.current_cargo.pop(del_cargo)
        except TypeError:
            print("Be attention")

    # Добавление груза

    def __add__(self, cargo):
        self.current_cargo.update(cargo)

    # Форматирование печати груза

    def format_cargo(self):
        print(f"Format cargo: {self.current_cargo.clear()}")

    # Вывод информации

    def __str__(self):
        return f"""
            Mark: {self.mark},
            Power: {self.power},
            Production year: {self.production_year},
            Maximum capacity: {self.maximum_capacity},
            Name and Surname: {self.name_surname},
            Current cargo: {self.current_cargo}"""


volvo = Truck('Volvo', 450, 2015, 2500, 'John Dodson', {'TV': 500, 'fridge': 500})
ford = Truck('Ford', 450, 2015, 2500, 'Jorge Masvidal', {'DVD': 100, 'fridge': 500})
daf = Truck('DAF', 500, 2020, 4500, 'Jay Ray', {'jeans': 4500, 'T-shirts': 5000})
if __name__ == '__main__':

    volvo + {'coat': 5000}
    daf + {'coat': 5000}
    volvo + {'shoes': 5000}
    print(volvo)
    print(daf)
