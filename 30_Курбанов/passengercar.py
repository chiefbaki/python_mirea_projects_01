from car import Car


class PassengerCar(Car):

    def __init__(self, mark, power, production_year, number_of_passengers, repair_book):
        super().__init__(mark, power, production_year)

        self.number_of_passenger = number_of_passengers
        self.repair_book = repair_book

    # Добавляем новые значения в старый словарь

    def __add__(self, repairs):
        self.repair_book.update(repairs)

    # Получаем дату замены запчасти

    def __getitem__(self, date_of_repair):
        return f"Date of repair: {self.repair_book.get(date_of_repair)}"

    # Форматируем печать ремонтной книжки

    def clear_repair_book(self):
        print(f"Repair book is clear: {self.repair_book.clear()}")

    # Получаем информацию

    def __str__(self):
        return f"""
            Mark: {self.mark},
            Power: {self.power},
            Production year: {self.production_year},
            Number of passengers: {self.number_of_passenger},
            Repair book: {self.repair_book}"""


mers = PassengerCar('Mercedes', 2005, 230, 20, {'brakes': 2021})
bmw = PassengerCar('BMW', 2002, 330, 25, {'reels': 2014})
if __name__ == '__main__':
    mers + {'eefef': 2013}
    print(mers['brakes'])
    print(bmw['reels'])
    print(mers)
    print(bmw)

