# Создать список (супермаркет), состоящий из словарей (товары). Словари должны содержать как минимум 5 полей
# (например, номер, наименование, отдел продажи, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# market = [{"id":123456, "product":"coca-cola 0.5", "department": "drinks", ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех товарах;
# – вывода информации о товаре по введенному с клавиатуры номеру;
# – вывода количества товаров, продающихся в определенном отделе;
# – обновлении всей информации о товаре по введенному номеру;
# – удалении товара по номеру.
# Провести тестирование функций.

def print_info(market):
    for k in market:
        print(k)

def num_of_info(market, n):
    print(market[n-1])
        
# def total(market):
#     departament_dict = dict()
#     for product in market:
#         departament_dict.setdefault(product["departament"], []).append(product["product"])
#     print(departament_dict)
        
def total(market):
    print( sum( map( lambda x: x[p], market) ) )

def updprod(market):
    a = int(input("ID : "))
    for i in market:
        if i["id"] == a:
            prodname = str(input("Введите новое название: "))
            depname = str(input("Введите отдел: "))
            sell = str(input("Введите количество продаж: "))
            mar2 = {"id": i["id"], "product": prodname, "department": depname, "numberOfSold": sell}
            i.update(mar2)
        print(i)


def del_info(market, n):
    market.pop(n)

market = [{"id": 1, "product": "coca-cola 0.5", "departament": "drinks", "numberOfSold": 20000}, 
          {"id": 2, "product": "pepsi 0.5", "departament": "drinks", "numberOfSold": 15500},
          {"id": 3, "product": "Fanta 1.5", "departament": "drinks", "numberOfSold": 7325},
          {"id": 4, "product": "sprite 1.0", "departament": "drinks", "numberOfSold": 11200},
          {"id": 5, "product": "snikers", "departament": "sweets", "numberOfSold": 19240},
          {"id": 6, "product": "twix", "departament": "sweets", "numberOfSold": 18399},
          {"id": 7, "product": "mars", "departament": "sweets", "numberOfSold": 16000},
          {"id": 8, "product": "dirol", "departament": "sweets", "numberOfSold": 34000},
          {"id": 9, "product": "orbit", "departament": "sweets", "numberOfSold": 31002},
          {"id": 10, "product": "eclipse", "departament": "sweets", "numberOfSold": 25000},
          {"id": 10, "product": "eclipse", "departament": "s", "numberOfSold": 2},
          {"id": 10, "product": "eclipse", "departament": "s", "numberOfSold": 2},]

# num = int(input("Enter num: "))
# num_of_info(market, num)

# p = input("Departament: ")
# total(market)
print(updprod(market))